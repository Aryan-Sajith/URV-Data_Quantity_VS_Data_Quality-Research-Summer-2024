import numpy as np
import matplotlib.pyplot as plt

# Data for the tables
data_size = [25, 50, 100]  # Percentage sizes
duplication_levels = [0, 25, 50, 75, 100]  # Duplication percentages

training_loss = [
    [3.1821, 3.1822, 3.1862],
    [2.5907, 2.6489, 2.6237],
    [2.0021, 1.9956, 1.9877],
    [1.1774, 1.2035, 1.1895],
    [0.0084, 0.0083, 0.0083]
]

valuation_accuracy = [
    [49.0200, 49.1978, 49.1947],
    [49.4500, 49.2684, 49.3294],
    [48.3034, 48.2553, 48.2316],
    [45.6222, 45.4552, 45.6691],
    [6.4844, 7.5622, 7.3472]
]

valuation_loss = [
    [3.1838, 3.1849, 3.1859],
    [3.1836, 3.1900, 3.1891],
    [3.2521, 3.2564, 3.2522],
    [3.4526, 3.4676, 3.4568],
    [12.2886, 12.2574, 12.0182]
]

valuation_perplexity = [
    [24.2228, 24.2482, 24.2707],
    [24.2176, 24.3762, 24.3521],
    [25.9363, 26.0492, 25.9400],
    [31.7007, 32.1755, 31.8266],
    [218062.2969, 211301.1562, 166426.7656]
]

def plot_with_breaks(data, title, ylabel, breaks, x_labels):
    """
    Plot data with specified y-axis breaks.
    
    Parameters:
    - data: List of lists, each containing data for different series.
    - title: Title of the plot.
    - ylabel: Label for the y-axis.
    - breaks: List of tuples, each specifying (y_min, y_max) for each subplot.
    - x_labels: Labels for the x-axis.
    """
    num_breaks = len(breaks)
    fig, axs = plt.subplots(num_breaks, 1, figsize=(8, 10), sharex=True)

    if num_breaks == 1:
        axs = [axs]  # Ensure axs is a list when there's only one subplot

    # Plot the lower range (smaller values) on top of the higher range
    for idx, (y_min, y_max) in enumerate(breaks):
        if idx == 1:
            axs[idx].set_xlabel(x_labels)
            axs[idx].set_ylabel(ylabel)
            for i, dup in enumerate(duplication_levels):
                axs[idx].plot(data_size, data[i], label=f'{dup}% Duplication')
            axs[idx].set_ylim(y_min, y_max)
            axs[idx].legend(loc='upper right')
            axs[idx].grid(True)

    # Plot the higher range (larger values) first to be on top
    for idx, (y_min, y_max) in enumerate(breaks):
        if idx == 0:
            axs[idx].set_title(title)
            axs[idx].set_ylabel(ylabel)
            for i, dup in enumerate(duplication_levels):
                axs[idx].plot(data_size, data[i], label=f'{dup}% Duplication')
            axs[idx].set_ylim(y_min, y_max)
            axs[idx].legend(loc='upper right')
            axs[idx].grid(True)

    plt.tight_layout()
    plt.show()

# Plot Training Loss
plot_with_breaks(training_loss, "Training Loss", "Loss", [(None, None)], 'Training Data Size (%)')

# Plot Valuation Loss with a y-axis break
plot_with_breaks(valuation_loss, "Valuation Loss", "Loss", [(11, 13), (3, 4)], 'Training Data Size (%)')

# Plot Valuation Accuracy with a y-axis break
plot_with_breaks(valuation_accuracy, "Valuation Accuracy", "Accuracy (%)", [(45, 50), (0, 10)], 'Training Data Size (%)')

# Plot Valuation Perplexity with a y-axis break
plot_with_breaks(valuation_perplexity, "Valuation Perplexity", "Perplexity", [(150000, 220000), (24, 35)], 'Training Data Size (%)')
