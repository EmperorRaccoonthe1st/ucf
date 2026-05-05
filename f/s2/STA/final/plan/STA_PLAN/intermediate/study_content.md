# Phase 2: Surgical Extraction - Study Content

## Q1a: Basic Statistical Terminology
- **Concept Name:** Basic Statistical Terminology
- **Core Definition:** Statistics is the science of collecting, describing, and interpreting data. A population is the entire group of interest, and a parameter describes it. A sample is a subset of the population, and a statistic describes the sample.
- **The Formula:** N/A
- **Requirements/Assumptions:** N/A
- **Calculator Hints:** N/A

## Q1b: Types of Data
- **Concept Name:** Types of Data
- **Core Definition:** Qualitative (categorical) variables classify individuals based on attributes, while quantitative variables provide numerical measures. Quantitative variables can be discrete (countable values) or continuous (measurable values).
- **The Formula:** N/A
- **Requirements/Assumptions:** N/A
- **Calculator Hints:** N/A

## Q1c: Levels of Measurement
- **Concept Name:** Levels of Measurement
- **Core Definition:** Variables are measured at four levels: Nominal (names/labels), Ordinal (ordered categories), Interval (meaningful differences, no true zero), and Ratio (meaningful ratios, true zero exists).
- **The Formula:** N/A
- **Requirements/Assumptions:** N/A
- **Calculator Hints:** N/A

## Q1d: Study Design
- **Concept Name:** Study Design
- **Core Definition:** Observational studies measure characteristics without influencing the outcome, showing association. Designed experiments intentionally apply treatments to observe effects, allowing for causation claims.
- **The Formula:** N/A
- **Requirements/Assumptions:** N/A
- **Calculator Hints:** N/A

## Q1e: Experimental Design
- **Concept Name:** Experimental Design
- **Core Definition:** Observational studies cannot prove causation due to lurking or confounding variables that may affect the response variable.
- **The Formula:** N/A
- **Requirements/Assumptions:** N/A
- **Calculator Hints:** N/A

## Q1f: Sampling Methods
- **Concept Name:** Sampling Methods
- **Core Definition:** In a simple random sample, every individual and every possible sample of size $n$ has an equal chance of being selected.
- **The Formula:** N/A
- **Requirements/Assumptions:** N/A
- **Calculator Hints:** Use `MATH` $\rightarrow$ `PRB` $\rightarrow$ `randInt(min, max, n)` to generate random integers.

## Q2a: Descriptive Statistics
- **Concept Name:** Descriptive Statistics
- **Core Definition:** The five-number summary describes the distribution of a dataset using the Minimum, First Quartile ($Q_1$), Median, Third Quartile ($Q_3$), and Maximum.
- **The Formula:** Formulas for Median and Quartiles
- **Requirements/Assumptions:** Data must be ordered from smallest to largest.
- **Calculator Hints:** Enter data in `L1`, then `STAT` $\rightarrow$ `CALC` $\rightarrow$ `1-Var Stats L1` to scroll down for the five-number summary.

## Q2b: Data Visualization (Boxplot)
- **Concept Name:** Data Visualization (Boxplot)
- **Core Definition:** A boxplot visually displays the five-number summary. The Interquartile Range (IQR) is used to identify outliers that fall beyond the established fences.
- **The Formula:** $IQR = Q_3 - Q_1$, Lower Fence $= Q_1 - 1.5(IQR)$, Upper Fence $= Q_3 + 1.5(IQR)$
- **Requirements/Assumptions:** N/A
- **Calculator Hints:** Use `STAT PLOT` and select the Boxplot with outliers icon to visualize.

## Q2c: Shape of Distribution
- **Concept Name:** Shape of Distribution
- **Core Definition:** The distance between quartiles in a boxplot reveals skewness. If the median is closer to $Q_1$, it is right-skewed; if closer to $Q_3$, it is left-skewed.
- **The Formula:** N/A
- **Requirements/Assumptions:** N/A
- **Calculator Hints:** N/A

## Q3a: Basic Probability
- **Concept Name:** Basic Probability
- **Core Definition:** Marginal probability is the likelihood of a single event occurring, typically found by dividing the row or column total by the grand total in a contingency table.
- **The Formula:** $P(A) = n(A) / N$
- **Requirements/Assumptions:** Outcomes must be equally likely.
- **Calculator Hints:** N/A

## Q3b: Probability Rules
- **Concept Name:** Probability Rules
- **Core Definition:** The General Addition Rule calculates the probability of event A or event B occurring, subtracting their intersection to avoid double-counting.
- **The Formula:** $P(A \cup B) = P(A) + P(B) - P(A \cap B)$
- **Requirements/Assumptions:** N/A
- **Calculator Hints:** N/A

## Q3c: Conditional Probability
- **Concept Name:** Conditional Probability
- **Core Definition:** The probability of event B occurring given that event A has already occurred, reducing the sample space to event A.
- **The Formula:** $P(B | A) = \frac{P(A \cap B)}{P(A)}$
- **Requirements/Assumptions:** $P(A) > 0$
- **Calculator Hints:** N/A

## Q3d: Independence of Events
- **Concept Name:** Independence of Events
- **Core Definition:** Two events are independent if knowing that one occurred does not change the probability of the other occurring.
- **The Formula:** $P(A \cap B) = P(A) \times P(B)$
- **Requirements/Assumptions:** N/A
- **Calculator Hints:** N/A

## Q3e: Multiplication Rule
- **Concept Name:** Multiplication Rule
- **Core Definition:** The general multiplication rule is used to calculate the probability of a sequence of dependent events occurring (e.g., drawing without replacement).
- **The Formula:** $P(A \cap B \cap C) = P(A) \times P(B|A) \times P(C|A \cap B)$
- **Requirements/Assumptions:** Used for dependent events (without replacement).
- **Calculator Hints:** N/A

## Q4a: Discrete Random Variables
- **Concept Name:** Discrete Random Variables
- **Core Definition:** A probability distribution lists all possible outcomes of a discrete random variable along with their corresponding probabilities.
- **The Formula:** $P(X=x) = n(x)/N$
- **Requirements/Assumptions:** $0 \le P(x) \le 1$ and $\sum P(x) = 1$
- **Calculator Hints:** N/A

## Q4b: Expected Value
- **Concept Name:** Expected Value
- **Core Definition:** The mean of a discrete random variable, representing the long-term average outcome over many trials.
- **The Formula:** $E(X) = \sum [x \times P(x)]$
- **Requirements/Assumptions:** N/A
- **Calculator Hints:** Put $x$ in `L1` and $P(x)$ in `L2`, then use `STAT` $\rightarrow$ `CALC` $\rightarrow$ `1-Var Stats L1, L2`.

## Q4c: Variance and Standard Deviation
- **Concept Name:** Variance and Standard Deviation
- **Core Definition:** The standard deviation measures the average spread or variability of a discrete random variable's outcomes around the expected value.
- **The Formula:** $\sigma = \sqrt{\sum [x^2 \times P(x)] - \mu^2}$
- **Requirements/Assumptions:** N/A
- **Calculator Hints:** `1-Var Stats L1, L2` provides $\sigma_x$ directly.

## Q4d: Binomial Distribution
- **Concept Name:** Binomial Distribution
- **Core Definition:** Calculates the probability of getting a specific number of successes in a fixed number of independent trials with a constant probability of success.
- **The Formula:** $P(X=x) = \binom{n}{x} p^x (1-p)^{n-x}$
- **Requirements/Assumptions:** Fixed number of trials $n$, independent trials, two mutually exclusive outcomes, and constant probability $p$.
- **Calculator Hints:** Use `2nd` $\rightarrow$ `VARS` $\rightarrow$ `binompdf(n, p, x)` for exactly $x$, and `binomcdf(n, p, x)` for $\le x$. For $P(X \ge x)$, compute $1 - \text{binomcdf}(n, p, x-1)$.

## Q4e: Binomial Distribution Properties
- **Concept Name:** Binomial Distribution Properties
- **Core Definition:** The mean gives the expected number of successes, and the standard deviation measures the typical deviation from the mean in a binomial setting.
- **The Formula:** $\mu = n \times p$, $\sigma = \sqrt{n \times p \times (1-p)}$
- **Requirements/Assumptions:** Same as binomial conditions.
- **Calculator Hints:** N/A

## Q5a: Sampling Distribution of the Sample Mean
- **Concept Name:** Sampling Distribution of the Sample Mean
- **Core Definition:** The distribution of all possible sample means of a given size. The standard error represents the standard deviation of these sample means.
- **The Formula:** $\mu_{\bar{x}} = \mu$, $\sigma_{\bar{x}} = \frac{\sigma}{\sqrt{n}}$
- **Requirements/Assumptions:** Independent observations, random sampling.
- **Calculator Hints:** N/A

## Q5b: Central Limit Theorem
- **Concept Name:** Central Limit Theorem
- **Core Definition:** The sampling distribution of the sample mean is approximately normal if the sample size is sufficiently large, enabling probability calculations using the standard normal model.
- **The Formula:** $Z = \frac{\bar{x} - \mu_{\bar{x}}}{\sigma_{\bar{x}}}$
- **Requirements/Assumptions:** $n \ge 30$ or the population distribution is normal.
- **Calculator Hints:** `2nd` $\rightarrow$ `VARS` $\rightarrow$ `normalcdf(lower, upper, \mu, \sigma/\sqrt{n})`

## Q5c: Sampling Distribution of Sample Proportion
- **Concept Name:** Sampling Distribution of Sample Proportion
- **Core Definition:** Before using the normal distribution for sample proportions, the expected number of successes and failures must both be at least 10.
- **The Formula:** $n \times p \ge 10$, $n \times (1-p) \ge 10$
- **Requirements/Assumptions:** The sample size must be $\le 5\%$ of the population size for independence.
- **Calculator Hints:** N/A

## Q5d: Sampling Distribution of Sample Proportion
- **Concept Name:** Sampling Distribution of Sample Proportion
- **Core Definition:** The mean and standard error describe the center and spread of the distribution of all possible sample proportions.
- **The Formula:** $\mu_{\hat{p}} = p$, $\sigma_{\hat{p}} = \sqrt{\frac{p(1-p)}{n}}$
- **Requirements/Assumptions:** $np \ge 10$ and $n(1-p) \ge 10$
- **Calculator Hints:** N/A

## Q5e: Sampling Distribution of Sample Proportion
- **Concept Name:** Sampling Distribution of Sample Proportion
- **Core Definition:** By converting a sample proportion to a Z-score, we can calculate the probability of observing a sample proportion within a certain range.
- **The Formula:** $Z = \frac{\hat{p} - \mu_{\hat{p}}}{\sigma_{\hat{p}}}$
- **Requirements/Assumptions:** Assumes the normal approximation conditions are met.
- **Calculator Hints:** `2nd` $\rightarrow$ `VARS` $\rightarrow$ `normalcdf(lower, upper, p, \sqrt{p(1-p)/n})`

## Q6a: Confidence Intervals for Proportions
- **Concept Name:** Confidence Intervals for Proportions
- **Core Definition:** A confidence interval provides a range of plausible values for the unknown population proportion based on the sample proportion and a margin of error.
- **The Formula:** $\hat{p} \pm z_{\alpha/2} \sqrt{\frac{\hat{p}(1-\hat{p})}{n}}$
- **Requirements/Assumptions:** $n\hat{p}(1-\hat{p}) \ge 10$, random sample.
- **Calculator Hints:** `STAT` $\rightarrow$ `TESTS` $\rightarrow$ `1-PropZInt` with $x$ (successes) and $n$ (sample size).

## Q6b: Confidence Intervals
- **Concept Name:** Confidence Intervals
- **Core Definition:** Interpreting the interval means stating we are a certain percentage confident that the true population parameter falls between the lower and upper bounds.
- **The Formula:** N/A
- **Requirements/Assumptions:** N/A
- **Calculator Hints:** N/A
