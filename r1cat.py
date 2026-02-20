import tkinter as tk
from tkinter import ttk
import threading
import time
import random
import sys

# =============================================================================
# CAT R1 - LOCAL WHITEPAPER ARCHITECTURE
# Python 3.14 / macOS M-series compatible
# Fix: removed rogue tk.Tk() in ThinkBlock, use sys.platform instead
# =============================================================================

class R1LocalLogicEngine:
    def __init__(self):
        self.is_ready = False

    def boot_sequence(self, status_callback):
        steps = [
            "Allocating Cat Interconnect Buffers...",
            "Loading MLA KV-Cache Projection...",
            "Initializing GRPO Reward Proxies...",
            "Routing MoE Experts [1-64]...",
            "Cat R1 (Offline Mode) Ready :3"
        ]
        for step in steps:
            status_callback(step)
            time.sleep(random.uniform(0.2, 0.4))
        self.is_ready = True

    def generate_response(self, query):
        selected = random.sample(range(1, 65), 4)
        yield ("debug", f"DEBUG: Routing through experts {selected}\n")

        thoughts = [
            f"Query: '{query}'. Analyzing constraints.",
            "Cross-referencing latent weights for logic-heavy intent.",
            "GRPO: Evaluating 5 parallel reasoning paths.",
            "Path 2 shows highest reward for correctness.",
            "MLA: Compressing KV-cache for high-density attention.",
            "Self-correction loop: Verifying cat-like persona.",
            "Reasoning complete."
        ]

        current_thought = ""
        for t in thoughts:
            current_thought += f"● {t}\n"
            yield ("thought", current_thought)
            time.sleep(0.3)

        finals = [
            "Based on my GRPO-trained logic, I am ready to assist. How can I help? :3",
            "Inference complete. MLA routing is optimal for your query. mrrp~",
            "Weights calibrated. Cat R1 online. Expert routing stable. owo",
            "Logic gates open. High-fidelity reasoning available. :3"
        ]

        answer = random.choice(finals)
        current = ""
        for char in answer:
            current += char
            yield ("answer", current)
            time.sleep(0.01)


class ThinkBlock(tk.Frame):
    """Collapsible reasoning block — no rogue Tk() calls."""
    def __init__(self, parent, colors):
        super().__init__(parent, bg=colors["bg"], pady=5)
        self.colors = colors

        # ✅ FIX: use sys.platform instead of tk.Tk().tk.call(...)
        mono = "Menlo" if sys.platform == "darwin" else (
            "Consolas" if sys.platform == "win32" else "DejaVu Sans Mono"
        )

        tk.Label(
            self, text="▼ Thought Process",
            font=("Arial", 9, "bold italic"),
            bg=colors["bg"], fg=colors["primary"], anchor="w"
        ).pack(fill="x")

        self.text_label = tk.Label(
            self, text="",
            font=(mono, 9),
            bg=colors["think_bg"], fg=colors["think_text"],
            justify="left", anchor="w", padx=10, pady=10,
            wraplength=550
        )
        self.text_label.pack(fill="x", pady=2)

    def update_text(self, content):
        self.text_label.config(text=content)


class CatR1App:
    def __init__(self, root):
        self.root = root
        self.root.title("Cat R1 - Local Reasoning Engine")
        self.root.geometry("1000x700")
        self.root.configure(bg="#050505")

        self.engine = R1LocalLogicEngine()

        self.colors = {
            "bg":         "#050505",
            "sidebar":    "#0f172a",
            "primary":    "#3b82f6",
            "bot_bubble": "#1e293b",
            "user_bubble":"#1d4ed8",
            "think_bg":   "#0f172a",
            "think_text": "#94a3b8",
            "border":     "#1e293b",
            "text_p":     "#f8fafc",
            "text_s":     "#64748b",
            "input_bg":   "#0f172a"
        }

        self.setup_ui()
        threading.Thread(
            target=self.engine.boot_sequence,
            args=(self.update_status,),
            daemon=True
        ).start()

    def setup_ui(self):
        # --- Sidebar ---
        self.sidebar = tk.Frame(self.root, width=250, bg=self.colors["sidebar"])
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)

        tk.Label(self.sidebar, text="CAT R1", font=("Arial", 18, "bold"),
                 bg=self.colors["sidebar"], fg=self.colors["primary"]).pack(pady=(20, 5))
        tk.Label(self.sidebar, text="Local MoE Inference", font=("Arial", 9),
                 bg=self.colors["sidebar"], fg=self.colors["text_s"]).pack()

        stats_frame = tk.Frame(self.sidebar, bg="#1e293b", padx=10, pady=10)
        stats_frame.pack(pady=20, padx=15, fill="x")

        for label, val in [("Architecture","Cat-MoE"),("Total","14B"),("Active","3B"),("Context","128k")]:
            f = tk.Frame(stats_frame, bg="#1e293b")
            f.pack(fill="x")
            tk.Label(f, text=label, bg="#1e293b", fg=self.colors["text_s"], font=("Arial", 8)).pack(side="left")
            tk.Label(f, text=val,   bg="#1e293b", fg=self.colors["text_p"], font=("Arial", 8, "bold")).pack(side="right")

        self.status_label = tk.Label(
            self.sidebar, text="Initializing...", font=("Arial", 8),
            bg=self.colors["sidebar"], fg=self.colors["primary"], wraplength=200
        )
        self.status_label.pack(side="bottom", pady=20)

        # --- Main chat ---
        self.main_container = tk.Frame(self.root, bg=self.colors["bg"])
        self.main_container.pack(side="right", fill="both", expand=True)

        self.canvas = tk.Canvas(self.main_container, bg=self.colors["bg"], highlightthickness=0)
        self.scroll_frame = tk.Frame(self.canvas, bg=self.colors["bg"])
        self.scrollbar = ttk.Scrollbar(self.main_container, orient="vertical", command=self.canvas.yview)

        self.canvas.create_window((0, 0), window=self.scroll_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="top", fill="both", expand=True, padx=20, pady=10)

        self.scroll_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        # --- Input bar ---
        input_bar = tk.Frame(self.main_container, bg=self.colors["bg"], pady=20, padx=20)
        input_bar.pack(side="bottom", fill="x")

        self.entry = tk.Entry(
            input_bar, bg=self.colors["input_bg"], fg="white",
            insertbackground="white", font=("Arial", 11), relief="flat",
            highlightthickness=1,
            highlightbackground=self.colors["border"],
            highlightcolor=self.colors["primary"]
        )
        self.entry.pack(side="left", fill="x", expand=True, ipady=8, padx=(0, 10))
        self.entry.bind("<Return>", lambda e: self.handle_send())

        tk.Button(
            input_bar, text="Send",
            bg=self.colors["primary"], fg="white",
            activebackground="#2563eb", relief="flat",
            font=("Arial", 10, "bold"),
            command=self.handle_send, padx=20
        ).pack(side="right")

    def update_status(self, msg):
        self.root.after(0, lambda: self.status_label.config(text=msg))

    def add_bubble(self, sender, text="", is_bot=False):
        wrapper = tk.Frame(self.scroll_frame, bg=self.colors["bg"], pady=10)
        wrapper.pack(fill="x", anchor="w")

        tk.Label(
            wrapper, text=sender, font=("Arial", 8, "bold"),
            bg=self.colors["bg"],
            fg=self.colors["primary"] if is_bot else self.colors["text_s"]
        ).pack(anchor="w", padx=5)

        bubble = tk.Label(
            wrapper, text=text,
            bg=self.colors["bot_bubble"] if is_bot else self.colors["user_bubble"],
            fg="white", font=("Arial", 10),
            justify="left", wraplength=600, padx=12, pady=8
        )
        bubble.pack(anchor="w", pady=2)
        self.root.after(10, lambda: self.canvas.yview_moveto(1.0))
        return bubble

    def handle_send(self):
        query = self.entry.get().strip()
        if not query or not self.engine.is_ready:
            return
        self.entry.delete(0, tk.END)
        self.add_bubble("YOU", query, False)
        threading.Thread(target=self.run_inference, args=(query,), daemon=True).start()

    def run_inference(self, query):
        wrapper = tk.Frame(self.scroll_frame, bg=self.colors["bg"], pady=10)
        wrapper.pack(fill="x", anchor="w")

        tk.Label(
            wrapper, text="CAT R1", font=("Arial", 8, "bold"),
            bg=self.colors["bg"], fg=self.colors["primary"]
        ).pack(anchor="w", padx=5)

        debug_label = tk.Label(wrapper, text="", font=("Courier", 8),
                               bg=self.colors["bg"], fg="#10b981")
        debug_label.pack(anchor="w")

        thought_block = ThinkBlock(wrapper, self.colors)
        thought_block.pack(fill="x", anchor="w", pady=5)

        answer_label = tk.Label(
            wrapper, text="",
            bg=self.colors["bot_bubble"], fg="white",
            font=("Arial", 10), justify="left",
            wraplength=600, padx=12, pady=8
        )
        answer_label.pack(anchor="w")

        for mode, content in self.engine.generate_response(query):
            if mode == "debug":
                self.root.after(0, lambda c=content: debug_label.config(text=c))
            elif mode == "thought":
                self.root.after(0, lambda c=content: thought_block.update_text(c))
            elif mode == "answer":
                self.root.after(0, lambda c=content: answer_label.config(text=c))
            self.root.after(0, lambda: self.canvas.yview_moveto(1.0))


if __name__ == "__main__":
    root = tk.Tk()
    app = CatR1App(root)
    root.mainloop()
