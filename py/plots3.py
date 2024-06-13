# ChatGPT 4o - https://chatgpt.com/share/76499bbc-95f7-48bf-8646-19786c1961f4
import matplotlib.pyplot as plt
import numpy as np

# Data
dimensions = [512, 768, 1024, 768, 1024, 1280, 1600, 2048, 4096, 6144, 12288, 
              512, 768, 1024, 1024, 1024, 768, 1024, 2048, 4096, 768, 20480]
model_sizes = [65e6, 110e6, 340e6, 124e6, 345e6, 774e6, 1.5e9, 2.7e9, 6.7e9, 
               13e9, 175e9, 60e6, 220e6, 770e6, 3e9, 11e9, 12e6, 18e6, 60e6, 
               235e6, 66e6, 530e9]

labels = [
    "Original Transformer", "BERT", "BERT", "GPT-2", "GPT-2", "GPT-2", "GPT-2", 
    "GPT-3", "GPT-3", "GPT-3", "GPT-3", "T5", "T5", "T5", "T5", "T5", 
    "ALBERT", "ALBERT", "ALBERT", "ALBERT", "DistilBERT", "Megatron-Turing NLG"
]

# Calculate log10 values
log_dimensions = np.log10(dimensions)
log_model_sizes = np.log10(model_sizes)

# Plotting
plt.figure(figsize=(10, 6))
plt.scatter(log_dimensions, log_model_sizes, color='blue')

# Adding labels for all points with specific offsets for T5 and BERT
xoff_default = -0.01
yoff_default = 0.1
xoff_specific = -0.02
yoff_specific = -0.05

for i, (x, y, label) in enumerate(zip(log_dimensions, log_model_sizes, labels)):
    if "T5" in label or "BERT" in label:
        plt.text(x + xoff_specific, y + yoff_specific, label, fontsize=9, ha='right')
    else:
        plt.text(x + xoff_default, y + yoff_default, label, fontsize=9, ha='right')

plt.title('Log10 of Model Dimension vs Log10 of Model Size')
plt.xlabel('Log10 of Model Dimension')
plt.ylabel('Log10 of Model Size')
plt.grid(True)

# Save as PDF
plt.savefig('Model_Dimensions_vs_Model_Sizes_Labeled.pdf')
plt.show()
