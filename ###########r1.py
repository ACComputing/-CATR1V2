import tkinter as tk
from tkinter import ttk, scrolledtext
import threading
import time
import random
import sys
import queue
import webbrowser

# =============================================================================
# CATSEEK R1 - LOCAL DESKTOP ARCHITECTURE
# Optimized for Python 3.14 & Cross-Platform UI
# =============================================================================

class CatInferenceEngine:
    """Simulates a reasoning Mixture of Experts (MoE) engine."""
    def __init__(self):
        self.is_ready = False
        self.model_mode = "Cat-R1" # Options: Cat-R1 (Reasoning), Cat-V3 (Standard)
        self.deep_mode = False      # deep thinking toggle

    def boot_sequence(self, callback):
        """Simulates model loading and weight allocation."""
        steps = [
            "Initializing MoE Router...",
            "Loading 64 Experts (37B active)...",
            "Allocating Multi-head Latent Attention (MLA)...",
            "Applying GRPO Reward Proxies...",
            "CatSeek R1 Engine Online :3"
        ]
        for step in steps:
            callback(step)
            time.sleep(random.uniform(0.1, 0.3))
        self.is_ready = True

    def generate(self, query, message_queue):
        """Streams thoughts and answers based on chosen model."""
        # 1. Expert Routing Metadata
        experts = random.sample(range(1, 65), 4)
        message_queue.put(("debug", f"Routing through Experts: {experts}"))

        if self.model_mode == "Cat-R1":
            # 2. Reasoning Phase (Chain of Thought)
            thoughts = [
                f"Analyzing user query: '{query}'",
                "Identifying core logical constraints...",
                "Recursive verification of cat-persona compliance.",
                "GRPO: Evaluating 5 parallel reasoning paths.",
                "Selecting path with highest reward for accuracy.",
                "Reasoning stabilized. Formatting output."
            ]
            
            # If deep mode is active, insert additional reasoning steps
            if self.deep_mode:
                deep_thoughts = [
                    "DeepThink: Exploring 12 additional reasoning branches...",
                    "DeepThink: Applying recursive self-consistency check.",
                    "DeepThink: Simulating counterfactual scenarios.",
                    "DeepThink: Final verification with ensemble of 8 experts."
                ]
                # Insert after the third thought
                thoughts[3:3] = deep_thoughts
            
            full_thought = ""
            for t in thoughts:
                full_thought += f"● {t}\n"
                message_queue.put(("thought", full_thought))
                time.sleep(0.4)

        # 3. Final Answer Phase
        responses = [
            "Based on my calculations and cat-logic, I have determined the answer is: mrrp! How can I help further? :3",
            "Logic gates confirm: CatSeek R1 is ready to assist. What's our next task? owo",
            "Calibration complete. My weights suggest this is the optimal response for a human friend!",
            "I've thought it over carefully. Here is your answer! *purrs logically*"
        ]
        
        answer = random.choice(responses)
        current_text = ""
        for char in answer:
            current_text += char
            message_queue.put(("answer", current_text))
            time.sleep(0.01) # Simulated typing speed
        
        message_queue.put(("done", None))

class CollapsibleThought(tk.Frame):
    """A DeepSeek-style collapsible reasoning block."""
    def __init__(self, parent, colors):
        super().__init__(parent, bg=colors["bg"], pady=10)
        self.colors = colors
        self.is_expanded = True

        self.header = tk.Frame(self, bg=colors["think_bg"], padx=10, pady=5)
        self.header.pack(fill="x")
        self.header.bind("<Button-1>", self.toggle)

        self.toggle_label = tk.Label(
            self.header, text="▼ Thought Process", 
            font=("Arial", 9, "bold italic"),
            bg=colors["think_bg"], fg=colors["primary"], cursor="hand2"
        )
        self.toggle_label.pack(side="left")
        self.toggle_label.bind("<Button-1>", self.toggle)

        self.content_frame = tk.Frame(self, bg=colors["think_bg"], padx=15, pady=10)
        self.content_frame.pack(fill="x")

        mono_font = "Menlo" if sys.platform == "darwin" else "Consolas"
        self.text_label = tk.Label(
            self.content_frame, text="", font=(mono_font, 9),
            bg=colors["think_bg"], fg=colors["think_text"],
            justify="left", anchor="w", wraplength=500
        )
        self.text_label.pack(fill="x")

    def toggle(self, event=None):
        self.is_expanded = not self.is_expanded
        if self.is_expanded:
            self.content_frame.pack(fill="x")
            self.toggle_label.config(text="▼ Thought Process")
        else:
            self.content_frame.pack_forget()
            self.toggle_label.config(text="▶ Show Thoughts")

    def update_text(self, content):
        self.text_label.config(text=content)

class CatSeekApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CatSeek R1 - Local Intelligence")
        self.root.geometry("1100x750")
        
        self.colors = {
            "bg": "#050505",
            "sidebar": "#0f172a",
            "primary": "#3b82f6",
            "border": "#1e293b",
            "user_bubble": "#1d4ed8",
            "bot_bubble": "#1e293b",
            "think_bg": "#0f172a",
            "think_text": "#94a3b8",
            "text_p": "#f8fafc",
            "text_s": "#64748b"
        }
        
        self.root.configure(bg=self.colors["bg"])
        self.engine = CatInferenceEngine()
        self.msg_queue = queue.Queue()
        self.deep_mode = False  # local deep mode flag for UI
        
        self.setup_styles()
        self.setup_ui()
        
        # Start background check for queue
        self.root.after(100, self.process_queue)
        
        # Boot the engine
        threading.Thread(target=self.engine.boot_sequence, args=(self.update_status,), daemon=True).start()

    def setup_styles(self):
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("Vertical.TScrollbar", gripcount=0, background=self.colors["border"], 
                        troughcolor=self.colors["bg"], bordercolor=self.colors["bg"], arrowcolor="white")

    def setup_ui(self):
        # --- Sidebar ---
        self.sidebar = tk.Frame(self.root, width=260, bg=self.colors["sidebar"], borderwidth=0)
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)

        tk.Label(self.sidebar, text="CatSeek R1", font=("Arial", 20, "bold"), 
                 bg=self.colors["sidebar"], fg=self.colors["primary"]).pack(pady=(30, 5))
        tk.Label(self.sidebar, text="Reasoning Engine", font=("Arial", 10), 
                 bg=self.colors["sidebar"], fg=self.colors["text_s"]).pack()

        # Model Selector
        tk.Label(self.sidebar, text="MODEL", font=("Arial", 8, "bold"), 
                 bg=self.colors["sidebar"], fg=self.colors["text_s"]).pack(anchor="w", padx=20, pady=(40, 5))
        
        self.model_var = tk.StringVar(value="Cat-R1")
        for m in ["Cat-R1", "Cat-V3"]:
            rb = tk.Radiobutton(self.sidebar, text=m, variable=self.model_var, value=m,
                                command=self.change_model, bg=self.colors["sidebar"], 
                                fg="white", selectcolor=self.colors["primary"], 
                                activebackground=self.colors["sidebar"], font=("Arial", 10))
            rb.pack(anchor="w", padx=30, pady=2)

        # Deepthink toggle button
        self.deepthink_btn = tk.Button(
            self.sidebar, text="🔍 Deepthink OFF", bg=self.colors["sidebar"],
            fg=self.colors["text_s"], font=("Arial", 10, "bold"), relief="flat",
            activebackground="#2563eb", activeforeground="white",
            command=self.toggle_deepthink
        )
        self.deepthink_btn.pack(anchor="w", padx=30, pady=(20, 5), fill="x")

        # Chat button (opens chat.deepseek.com)
        self.chat_btn = tk.Button(
            self.sidebar, text="💬 Chat.deepseek.com", bg=self.colors["primary"],
            fg="white", font=("Arial", 10, "bold"), relief="flat",
            activebackground="#2563eb", command=self.open_chat
        )
        self.chat_btn.pack(anchor="w", padx=30, pady=5, fill="x")

        # Status
        self.status_label = tk.Label(self.sidebar, text="Initializing...", font=("Arial", 8),
                                     bg=self.colors["sidebar"], fg=self.colors["primary"], wraplength=220)
        self.status_label.pack(side="bottom", pady=20)

        # --- Main Chat ---
        self.main_container = tk.Frame(self.root, bg=self.colors["bg"])
        self.main_container.pack(side="right", fill="both", expand=True)

        # Scrolling Area
        self.canvas = tk.Canvas(self.main_container, bg=self.colors["bg"], highlightthickness=0)
        self.scroll_frame = tk.Frame(self.canvas, bg=self.colors["bg"])
        self.scrollbar = ttk.Scrollbar(self.main_container, orient="vertical", command=self.canvas.yview)

        self.canvas.create_window((0, 0), window=self.scroll_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="top", fill="both", expand=True, padx=40, pady=20)

        self.scroll_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        # Input Area
        input_frame = tk.Frame(self.main_container, bg=self.colors["bg"], pady=20, padx=40)
        input_frame.pack(side="bottom", fill="x")

        self.entry = tk.Entry(input_frame, bg=self.colors["sidebar"], fg="white", 
                             insertbackground="white", font=("Arial", 12), relief="flat",
                             highlightthickness=1, highlightbackground=self.colors["border"],
                             highlightcolor=self.colors["primary"])
        self.entry.pack(side="left", fill="x", expand=True, ipady=10, padx=(0, 15))
        self.entry.bind("<Return>", lambda e: self.send_message())

        self.send_btn = tk.Button(input_frame, text="Send", bg=self.colors["primary"], fg="white",
                                 font=("Arial", 10, "bold"), relief="flat", padx=25,
                                 command=self.send_message, activebackground="#2563eb")
        self.send_btn.pack(side="right")

    def toggle_deepthink(self):
        """Toggle deep thinking mode and update button appearance."""
        self.deep_mode = not self.deep_mode
        self.engine.deep_mode = self.deep_mode  # sync with engine
        if self.deep_mode:
            self.deepthink_btn.config(
                text="🔍 Deepthink ON",
                fg=self.colors["primary"],
                bg=self.colors["border"]  # use border color for consistency
            )
        else:
            self.deepthink_btn.config(
                text="🔍 Deepthink OFF",
                fg=self.colors["text_s"],
                bg=self.colors["sidebar"]
            )
        self.update_status(f"DeepThink {'enabled' if self.deep_mode else 'disabled'}")

    def open_chat(self):
        """Open chat.deepseek.com in default web browser."""
        webbrowser.open("https://chat.deepseek.com")

    def update_status(self, msg):
        self.root.after(0, lambda: self.status_label.config(text=msg))

    def change_model(self):
        self.engine.model_mode = self.model_var.get()
        self.update_status(f"Switched to {self.engine.model_mode}")

    def send_message(self):
        query = self.entry.get().strip()
        if not query or not self.engine.is_ready:
            return
        
        self.entry.delete(0, tk.END)
        self.add_bubble("YOU", query, False)
        
        # Start Inference
        self.active_thought_block = None
        self.active_answer_label = None
        self.current_wrapper = self.create_bot_wrapper()
        
        threading.Thread(target=self.engine.generate, args=(query, self.msg_queue), daemon=True).start()

    def add_bubble(self, sender, text, is_bot):
        wrapper = tk.Frame(self.scroll_frame, bg=self.colors["bg"], pady=10)
        wrapper.pack(fill="x", anchor="w")

        tk.Label(wrapper, text=sender, font=("Arial", 8, "bold"),
                 bg=self.colors["bg"], fg=self.colors["primary"] if is_bot else self.colors["text_s"]).pack(anchor="w")

        bubble = tk.Label(wrapper, text=text, bg=self.colors["bot_bubble"] if is_bot else self.colors["user_bubble"],
                         fg="white", font=("Arial", 11), justify="left", wraplength=550, padx=15, pady=10)
        bubble.pack(anchor="w", pady=5)
        
        self.root.after(10, lambda: self.canvas.yview_moveto(1.0))
        return bubble

    def create_bot_wrapper(self):
        wrapper = tk.Frame(self.scroll_frame, bg=self.colors["bg"], pady=10)
        wrapper.pack(fill="x", anchor="w")
        
        tk.Label(wrapper, text="CATSEEK R1", font=("Arial", 8, "bold"),
                 bg=self.colors["bg"], fg=self.colors["primary"]).pack(anchor="w")
        
        self.debug_label = tk.Label(wrapper, text="", font=("Courier", 8), bg=self.colors["bg"], fg="#10b981")
        self.debug_label.pack(anchor="w")
        
        return wrapper

    def process_queue(self):
        try:
            while True:
                mode, content = self.msg_queue.get_nowait()
                if mode == "debug":
                    self.debug_label.config(text=content)
                elif mode == "thought":
                    if not self.active_thought_block:
                        self.active_thought_block = CollapsibleThought(self.current_wrapper, self.colors)
                        self.active_thought_block.pack(fill="x", pady=5)
                    self.active_thought_block.update_text(content)
                elif mode == "answer":
                    if not self.active_answer_label:
                        self.active_answer_label = tk.Label(self.current_wrapper, text="", bg=self.colors["bot_bubble"],
                                                          fg="white", font=("Arial", 11), justify="left", 
                                                          wraplength=550, padx=15, pady=10)
                        self.active_answer_label.pack(anchor="w", pady=5)
                    self.active_answer_label.config(text=content)
                elif mode == "done":
                    pass
                
                self.canvas.yview_moveto(1.0)
        except queue.Empty:
            pass
        finally:
            self.root.after(50, self.process_queue)

if __name__ == "__main__":
    root = tk.Tk()
    app = CatSeekApp(root)
    root.mainloop()
