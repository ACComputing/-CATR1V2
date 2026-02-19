import tkinter as tk
from tkinter import font
import threading
import time
import random

# =============================================================================
# CAT R1 - LOCAL WHITEPAPER ARCHITECTURE (NO-API EDITION)
# -----------------------------------------------------------------------------
# SPECIFICATIONS:
# - Training: Simulated GRPO (Group Relative Policy Optimization)
# - Architecture: Cat-MoE (14B Total / 3B Active)
# - Inference: MLA (Multi-head Latent Attention) @ 128k Context
# - Efficiency: Local Reasoner (Deterministic Logic Engine)
# =============================================================================

class R1LocalLogicEngine:
    """Simulates R1's internal reasoning loops without any network calls."""
    def __init__(self):
        self.is_ready = False
        # Whitepaper stats
        self.total_params = "14B"
        self.active_params = "3B"
        self.experts = 64
        self.active_experts = 4

    def boot_sequence(self, status_callback):
        """Simulates the loading of MoE experts into VRAM clusters."""
        steps = [
            "Allocating Cat Interconnect Buffers...",
            "Loading MLA KV-Cache Projection Matrix...",
            "Initializing GRPO Reward Proxies...",
            "Routing MoE Experts [1-64]...",
            "Cat R1 (Offline Mode) Ready :3"
        ]
        for step in steps:
            status_callback(step)
            time.sleep(random.uniform(0.3, 0.6))
        self.is_ready = True

    def get_whitepaper_reasoning(self, query):
        """Generates a high-fidelity Chain of Thought (CoT)."""
        
        # Step 1: Simulated Expert Routing
        selected = random.sample(range(1, 65), 4)
        yield f"DEBUG: Routing through experts {selected}\n"
        
        # Step 2: The <think> block simulation
        thoughts = [
            f"User Query: '{query}'. Identifying primary intent.",
            "Retrieving latent space embeddings for structural mapping.",
            "GRPO Step 1: Generating 5 parallel reasoning branches.",
            "Branch 3 shows higher relative advantage for logic-heavy response.",
            "GRPO Step 2: Self-correction loop initiated. Verifying constraints.",
            "MLA check: Optimizing attention weights for syntax precision.",
            "Reasoning chain finalized. Formatting output for safety and clarity."
        ]
        
        thought_str = "<think>\n"
        for t in thoughts:
            thought_str += f"● {t}\n"
            time.sleep(0.4)
            yield thought_str

        thought_str += "</think>\n\n"
        yield thought_str

        # Step 3: Final Answer Generation
        final_templates = [
            "Based on my internal reasoning logic (Cat R1 framework), I have processed your request. How can I assist you with math, coding, or general questions today? :3",
            "System check complete. MLA routing confirms optimal token density. I am ready to provide logical and safe assistance within this local environment. meow~",
            "Executing output. My GRPO-trained weights suggest that a direct, logical approach is most efficient for your query. What's our next task? owo",
            "Reinforcement learning weights have been calibrated for this session. I am operating as Cat R1, your local reasoning assistant. :3"
        ]
        
        base_answer = thought_str + random.choice(final_templates)
        tokens = base_answer.split()
        
        current_text = ""
        for token in tokens:
            current_text += token + " "
            yield current_text
            time.sleep(0.02)

class CatR1App:
    def __init__(self, root):
        self.root = root
        self.root.title("Cat R1 - chat.deepseek.com style")
        self.root.geometry("1000x650")
        self.root.configure(bg="#0d0d0d")

        self.engine = R1LocalLogicEngine()
        
        self.colors = {
            "bg": "#0d0d0d",
            "sidebar": "#1a1a1a",
            "primary": "#3b82f6",
            "bot_bubble": "#2d2d2d",
            "user_bubble": "#1e3a8a",
            "think_text": "#9ca3af",
            "border": "#333333",
            "text_primary": "#ffffff",
            "text_secondary": "#a0a0a0",
            "input_bg": "#262626",
            "black_button": "#1a1a1a"
        }

        self.setup_ui()
        threading.Thread(target=self.engine.boot_sequence, args=(self.update_status,), daemon=True).start()

    def setup_ui(self):
        default_font = font.nametofont("TkDefaultFont")
        default_font.configure(size=10)
        self.root.option_add("*Font", default_font)

        # Sidebar
        self.sidebar = tk.Frame(self.root, width=260, bg=self.colors["sidebar"], highlightthickness=0)
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)

        # New Chat button — black bg, blue text
        new_chat_btn = tk.Button(
            self.sidebar,
            text="+ New Chat",
            bg=self.colors["black_button"],
            fg=self.colors["primary"],
            activebackground="#333333",
            activeforeground=self.colors["primary"],
            relief="flat",
            font=("Arial", 11, "bold"),
            padx=10,
            pady=8,
            borderwidth=0,
            command=self.new_chat
        )
        new_chat_btn.pack(pady=(20, 10), padx=15, fill="x")

        # Model info card
        model_frame = tk.Frame(self.sidebar, bg=self.colors["sidebar"])
        model_frame.pack(pady=5, padx=15, fill="x")

        tk.Label(
            model_frame,
            text="Cat R1  :3",
            font=("Arial", 14, "bold"),
            bg=self.colors["sidebar"],
            fg=self.colors["text_primary"]
        ).pack(anchor="w")

        details = [
            ("Architecture", "Cat-MoE"),
            ("Total Params", "14B"),
            ("Active Params", "3B"),
            ("Optimizer", "GRPO"),
            ("Experts", "64 (4 active)")
        ]
        for label, value in details:
            row = tk.Frame(model_frame, bg=self.colors["sidebar"])
            row.pack(anchor="w", pady=2)
            tk.Label(row, text=f"{label}:", bg=self.colors["sidebar"], fg=self.colors["text_secondary"], width=12, anchor="w").pack(side="left")
            tk.Label(row, text=value, bg=self.colors["sidebar"], fg=self.colors["text_primary"], anchor="w").pack(side="left")

        sep = tk.Frame(self.sidebar, height=1, bg=self.colors["border"])
        sep.pack(fill="x", pady=15, padx=15)

        self.status_label = tk.Label(
            self.sidebar,
            text="Powering up...",
            font=("Arial", 9),
            bg=self.colors["sidebar"],
            fg=self.colors["text_secondary"],
            wraplength=220,
            justify="left"
        )
        self.status_label.pack(side="bottom", pady=20, padx=15)

        # Main chat area
        self.chat_container = tk.Frame(self.root, bg=self.colors["bg"])
        self.chat_container.pack(side="right", fill="both", expand=True)

        self.msg_canvas = tk.Canvas(self.chat_container, bg=self.colors["bg"], highlightthickness=0)
        self.msg_frame = tk.Frame(self.msg_canvas, bg=self.colors["bg"])
        self.scrollbar = tk.Scrollbar(self.chat_container, orient="vertical", command=self.msg_canvas.yview, bg=self.colors["border"])
        
        self.msg_canvas.create_window((0, 0), window=self.msg_frame, anchor="nw")
        self.msg_canvas.configure(yscrollcommand=self.scrollbar.set)
        self.msg_canvas.pack(side="top", fill="both", expand=True, padx=10, pady=10)
        self.scrollbar.pack(side="right", fill="y")
        
        self.msg_frame.bind("<Configure>", lambda e: self.msg_canvas.configure(scrollregion=self.msg_canvas.bbox("all")))

        # Input area
        self.input_frame = tk.Frame(self.chat_container, bg=self.colors["bg"], pady=20)
        self.input_frame.pack(side="bottom", fill="x", padx=20)

        self.entry = tk.Entry(
            self.input_frame,
            font=("Arial", 11),
            bg=self.colors["input_bg"],
            fg=self.colors["text_primary"],
            insertbackground=self.colors["text_primary"],
            borderwidth=1,
            relief="solid",
            highlightbackground=self.colors["border"],
            highlightcolor=self.colors["primary"],
            highlightthickness=1
        )
        self.entry.pack(side="left", fill="x", expand=True, ipady=10, padx=(0, 10))
        self.entry.insert(0, "Ask anything... meow~")
        self.entry.bind("<FocusIn>", self.clear_placeholder)
        self.entry.bind("<FocusOut>", self.restore_placeholder)
        self.entry.bind("<Return>", lambda e: self.send_message())

        # Send button — black bg, blue text
        self.send_btn = tk.Button(
            self.input_frame,
            text="Send",
            font=("Arial", 10, "bold"),
            bg=self.colors["black_button"],
            fg=self.colors["primary"],
            activebackground="#333333",
            activeforeground=self.colors["primary"],
            relief="flat",
            padx=20,
            pady=10,
            command=self.send_message,
            borderwidth=0
        )
        self.send_btn.pack(side="right")

        self.placeholder_active = True

    def clear_placeholder(self, event):
        if self.placeholder_active:
            self.entry.delete(0, tk.END)
            self.entry.config(fg=self.colors["text_primary"])
            self.placeholder_active = False

    def restore_placeholder(self, event):
        if not self.entry.get().strip():
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "Ask anything... meow~")
            self.entry.config(fg=self.colors["text_secondary"])
            self.placeholder_active = True

    def new_chat(self):
        for widget in self.msg_frame.winfo_children():
            widget.destroy()

    def update_status(self, msg):
        self.root.after(0, lambda: self.status_label.config(text=msg))

    def add_message(self, sender, text=""):
        is_user = (sender == "You")
        wrapper = tk.Frame(self.msg_frame, bg=self.colors["bg"], pady=8)
        wrapper.pack(fill="x", padx=10)
        
        bubble_color = self.colors["user_bubble"] if is_user else self.colors["bot_bubble"]
        text_color = self.colors["text_primary"]
        
        bubble = tk.Message(
            wrapper,
            text=text,
            bg=bubble_color,
            fg=text_color,
            font=("Arial", 10),
            width=600,
            justify="left",
            padx=15,
            pady=10,
            borderwidth=0
        )
        bubble.pack(side="right" if is_user else "left")
        
        self.root.update_idletasks()
        self.msg_canvas.yview_moveto(1.0)
        return bubble

    def send_message(self):
        if self.placeholder_active:
            return
        query = self.entry.get().strip()
        if not query or not self.engine.is_ready:
            return
        self.entry.delete(0, tk.END)
        self.restore_placeholder(None)
        self.add_message("You", query)
        threading.Thread(target=self.run_logic, args=(query,)).start()

    def run_logic(self, query):
        bubble = self.add_message("Cat R1", "Routing experts... :3")
        
        for reasoning_text in self.engine.get_whitepaper_reasoning(query):
            self.root.after(0, lambda t=reasoning_text: bubble.config(text=t))
            
            if "<think>" in reasoning_text and "</think>" not in reasoning_text:
                self.root.after(0, lambda: bubble.config(fg=self.colors["think_text"]))
            else:
                self.root.after(0, lambda: bubble.config(fg=self.colors["text_primary"]))
            
            self.root.after(0, lambda: self.msg_canvas.yview_moveto(1.0))

if __name__ == "__main__":
    root = tk.Tk()
    try:
        from ctypes import windll
        windll.shcore.SetProcessDpiAwareness(1)
    except:
        pass
    app = CatR1App(root)
    root.mainloop()
c
