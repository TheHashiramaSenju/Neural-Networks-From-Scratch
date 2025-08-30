# Neural Networks Notes and Implementations

Concise, practical notes and minimal implementations across perceptrons, multilayer perceptrons, and convolutional neural networks. High-level "Concepts" offer quick intuition, while "Internal-details.md" captures deeper derivations, math, and design trade-offs.

## Repository Overview

This repository is organized by model family. Each folder contains two documentation layers to aid both quick revision and deep study:

- **Concepts** (notes.md): a bird's-eye narrative of what and why for each topic
- **Internal-details.md**: deeper mechanics, derivations, and edge cases



## What Each Part Contains

### ANNs and Perceptrons
- **notes.md**: high-level concepts, linear decision boundaries, step vs. sigmoid activations, and perceptron convergence intuition
- **Internal-details.md**: margin, separability assumptions, perceptron updates and loss variants, connections to logistic regression
- **.py files**: training loop with mistake-driven updates and toy-data evaluation

### Multilayer Perceptron Architecture
- **notes.md**: intuition for depth and hidden layers, nonlinearity (ReLU, tanh), overfitting risks, and common training recipes
- **Internal-details.md**: forward/backprop equations, parameter shapes, initialization, regularization (L2, dropout)

### Convolutional Neural Networks
- **notes.md**: CNN intuition—locality, weight sharing, receptive fields, pooling—and when CNNs are preferable
- **Internal-details.md**: convolution/pooling operators, padding/stride math, feature-map sizing, and common architectural patterns

## Getting Started

### Prerequisites
- Python 3.9+
- NumPy
- Matplotlib/Seaborn
- scikit-learn for toy datasets

### Suggested Reading Flow
1. Skim `notes.md` for intuition
2. Study `Internal-details.md` for mechanics
3. Run any provided minimal implementation


### Future Additions
- Add `requirements.txt` for reproducibility
- Consider "Open in Colab" badges as the repository grows

## Learning Goals

- Build an intuition-first map of core neural architectures for quick recall
- Maintain deeper derivations in Internal-details.md to support rigorous understanding and future expansion

## Contributing

- Open issues or pull requests for fixes, clarifications, or new minimal examples
- Keep notes concise and runnable code small
- Follow a simple style: one concept per paragraph, short code blocks, and targeted figures where helpful

## Roadmap

- [ ] Add minimal MLP example with training loop
- [ ] Add small CNN demo (e.g., MNIST-like)
- [ ] Add `requirements.txt`
- [ ] Add optional badges (Python version, license)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Documentation Style

- Keep README as the entry point answering what, why, and how
- Place deeper derivations per topic in `Internal-details.md`
- Use clear Markdown headings, lists, and fenced code blocks
- Update the overview section when new folders/examples are added

---

**Note**: This repository serves as a personal learning log and reference guide for neural network fundamentals. Feel free to use, modify, and contribute to improve the documentation and examples.
