# Student Performance Analysis Using Python

## Project Overview

This project performs Exploratory Data Analysis (EDA) on a student performance dataset. The goal is to analyze student attendance, subject-wise marks, overall performance, and identify patterns that affect academic results.

## Objectives

* Assess the quality of the dataset.
* Clean and preprocess the data.
* Calculate total marks and percentage.
* Analyze attendance and academic performance.
* Visualize key insights using charts and graphs.

## Dataset Information

The dataset contains the following columns:

* Student_ID
* Name
* Gender
* Age
* Attendance
* Maths
* Science
* English

## Technologies Used

* Python
* Pandas
* Matplotlib
* Jupyter Notebook

## Project Structure

Student_Performance_Project/

├── data_students.csv

├── notebook_student_eda.ipynb

├── processed/

│ └── cleaned_students.csv

├── reports.md

└── README.md

## Data Assessment

The dataset was examined for:

* Missing values
* Duplicate records
* Data types
* Dataset dimensions

## Data Cleaning

The following preprocessing steps were performed:

* Removed duplicate records
* Created Total Marks column
* Created Percentage column
* Generated a cleaned dataset

## Exploratory Data Analysis

The following analyses were performed:

1. Attendance Distribution
2. Gender Distribution
3. Attendance vs Percentage
4. Subject-wise Average Marks
5. Student Performance Ranking

## Key Findings

* Students with higher attendance generally achieved higher percentages.
* Subject performance was consistent across the dataset.
* Top-performing students were identified based on overall percentage.

## Output Files

* Cleaned Dataset (`cleaned_students.csv`)
* EDA Notebook (`notebook_student_eda.ipynb`)
* Analysis Report (`reports.md`)

## Conclusion

This project demonstrates the complete EDA workflow including dataset assessment, cleaning, visualization, and insight generation using Python.
