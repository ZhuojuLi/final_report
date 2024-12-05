import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the uploaded CSV file to examine its contents
# file_path = 'gym_members_exercise_tracking_synthetic_data.csv'
file_path = 'cleaned_gym_members_data.csv'
data = pd.read_csv(file_path)

# Setting up the figure layout
fig = plt.figure(figsize=(16, 9))
grid = plt.GridSpec(2, 3, hspace=0.6, wspace=0.4)

# Main plot: Relationship between Session Duration and Calories Burned, colored by Workout Type
main_ax = fig.add_subplot(grid[:, :2])
sns.scatterplot(
    data=data,
    x="Session_Duration (hours)",
    y="Calories_Burned",
    hue="Workout_Type",
    style="Workout_Type",
    ax=main_ax
)
main_ax.set_title("Session Duration vs. Calories Burned", fontsize=14)
main_ax.set_xlabel("Session Duration (hours)", fontsize=12)
main_ax.set_ylabel("Calories Burned", fontsize=12)
main_ax.legend(title="Workout Type", fontsize=10, title_fontsize=12, loc='upper left')

# Side Panel 1: Distribution of Calories Burned
side_ax1 = fig.add_subplot(grid[0, 2])
sns.histplot(
    data=data,
    x="Calories_Burned",
    kde=True,
    ax=side_ax1,
    bins=20,
    color="skyblue",
)
side_ax1.set_title("Distribution of Calories Burned", fontsize=14)
side_ax1.set_xlabel("Calories Burned", fontsize=12)
side_ax1.set_ylabel("Frequency", fontsize=12)

# Side Panel 2: Average Resting BPM by Workout Frequency with adjusted y-axis range
side_ax2 = fig.add_subplot(grid[1, 2])
avg_bpm_data = data.groupby("Workout_Frequency (days/week)")["Resting_BPM"].mean()
avg_bpm_data.plot(kind="bar", ax=side_ax2, color="orange")
side_ax2.set_ylim(63, 66)

# Titles and labels
side_ax2.set_title("Average Resting BPM by Workout Frequency", fontsize=14)
side_ax2.set_xlabel("Workout Frequency (days/week)", fontsize=12)
side_ax2.set_ylabel("Average Resting BPM", fontsize=12)

# Adjust layout manually to fix overlapping elements
plt.suptitle("Gym Member Exercise and Health Metrics Analysis", fontsize=16, y=0.98)
plt.subplots_adjust(top=0.88)
plt.show()
