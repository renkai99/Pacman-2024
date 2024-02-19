# Learning to play Pacman

This repository contains the code for a simple implementation of the Pacman game using the Gymnasium library. The template set up a basic environment for running the game and it will be used for the Ing Simultanée projects 2024 at Sycamore lab, EPFL.

## Prerequisites

Before you start, ensure you have the following installed on your system:

- Python 3.7 or higher
- pip (Python package installer)

## Dependencies

To run the Pacman game, you need to install the following Python packages:

- `gymnasium` - for creating and managing the game environment
- `numpy` - for numerical operations
- `matplotlib` (optional) - for visualizations and plotting

You can install these dependencies by running the following command in your terminal:

```bash
pip install gymnasium numpy matplotlib
```

## Installation

To get started with the Pacman game, follow these steps:

1. **Clone the Repository**

   Clone this repository to your local machine using the following command:

   ```bash
   git clone https://github.com/renkai99/Pacman-2024.git
   ```

2. **Navigate to the Repository Directory**

   Change into the repository directory:

   ```bash
   cd pacman-gym
   ```

3. **Install Dependencies**

   Install the required Python packages listed above by running:

   ```bash
   pip install -r requirements.txt
   ```

## Running the Game

To run the Pacman game with a random policy, execute the following command in the terminal:

```bash
python pacman.py
```

This script initializes the Pacman game environment and controls the agent with a random policy. It will run through episodes of the game, taking random actions at each step.

## Contributions

Contributions to this project are welcome. Please fork the repository, make your changes, and submit a pull request.
