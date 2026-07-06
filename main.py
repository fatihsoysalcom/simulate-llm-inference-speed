import time
import random

def simple_llm_inference(prompt: str, max_tokens: int = 50, compute_delay_per_token_ms: int = 10):
    """
    Simulates a very basic LLM inference process, generating tokens one by one.
    This example highlights the sequential nature of token generation and
    the computational effort (simulated by delay) per token, which specialized
    AI chips aim to accelerate for real-time LLM serving.
    """
    print(f"Prompt: '{prompt}'")
    generated_text = list(prompt.split())
    
    # A very simple "vocabulary" for demonstration (Turkish words related to the article topic)
    vocabulary = [
        "yapay", "zeka", "modelleri", "hızla", "gelişiyor", "ve", 
        "yeni", "donanımlar", "gerektiriyor", "bu", "süreçte", "özel", 
        "çipler", "önemli", "rol", "oynuyor", "çıkarım", "işlemleri", 
        "için", "optimize", "edilmiş", "donanım", "kritik", "öneme", "sahip"
    ]
    
    start_time = time.perf_counter()
    
    print("Generated: ", end="")
    for i in range(max_tokens):
        # Simulate computation for generating one token.
        # In real LLMs, this involves complex matrix multiplications and activations.
        # Specialized hardware (like TPUs, Inferentia2, Groq LPU) optimizes this step
        # to reduce this 'compute_delay_per_token_ms' significantly.
        time.sleep(compute_delay_per_token_ms / 1000.0) 
        
        # Simple token generation logic: just pick a random word from vocabulary.
        # A real LLM would predict the most probable next token based on context.
        next_token = random.choice(vocabulary)
        generated_text.append(next_token)
        
        # Print token as it's generated (simulating streaming output).
        print(next_token, end=" ", flush=True) 
        
        # Simulate early stopping condition for some variability.
        if len(generated_text) > 5 and random.random() < 0.05:
            break
            
    end_time = time.perf_counter()
    
    # Calculate tokens generated, excluding prompt tokens.
    total_tokens_generated = len(generated_text) - len(prompt.split())
    duration = end_time - start_time
    
    print(f"\n\n--- Inference Summary ---")
    print(f"Total tokens generated: {total_tokens_generated}")
    print(f"Total inference time: {duration:.2f} seconds")
    if duration > 0:
        tokens_per_second = total_tokens_generated / duration
        print(f"Tokens per second (TPS): {tokens_per_second:.2f} TPS")
    else:
        print("Duration too short to calculate TPS accurately.")

if __name__ == "__main__":
    # The article discusses LLM serving and the importance of speed (tokens per second).
    # This simulation demonstrates how even a small delay per token can add up,
    # highlighting the need for highly optimized hardware for real-time inference.
    
    # Example 1: Default simulation (moderate delay per token)
    print("--- Running Simulation 1: Default Delay (10ms/token) ---")
    simple_llm_inference(
        prompt="Yapay zeka çiplerinde yeni dönem",
        max_tokens=30,
        compute_delay_per_token_ms=10 # Simulates computational load per token
    )
    print("\n" + "="*70 + "\n")

    # Example 2: Faster simulation (e.g., what specialized hardware aims for)
    print("--- Running Simulation 2: Reduced Delay (2ms/token) ---")
    simple_llm_inference(
        prompt="LLM modellerinin çıkarım hızı",
        max_tokens=30,
        compute_delay_per_token_ms=2 # Simulates faster processing by specialized hardware
    )
    print("\n" + "="*70 + "\n")

    # Example 3: Slower simulation (e.g., a less optimized setup or heavier model)
    print("--- Running Simulation 3: Increased Delay (50ms/token) ---")
    simple_llm_inference(
        prompt="Gerçek zamanlı yapay zeka",
        max_tokens=20,
        compute_delay_per_token_ms=50 # Simulates slower processing
    )
    print("\n" + "="*70 + "\n")