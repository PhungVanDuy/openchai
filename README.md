# OpenChai

### Installation:
1. Install axolotl
```bash
pip3 install -U git+https://github.com/huggingface/peft.git
git clone https://github.com/OpenAccess-AI-Collective/axolotl
cd axolotl
pip3 install -e .[flash-attn]
```
2. Install OpenChai
```bash
git clone https://github.com/PhungVanDuy/openchai.git
cd openchai
pip3 install -e .
```

### Training:
Example:

```bash
openchai train --config_path examples/llama2/7b_chatml.yaml
```

### Submit model

### Chat with your model
