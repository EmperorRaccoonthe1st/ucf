# STA 2023 - Draft Answer Key (New Version)

## Question 1 Solutions

### (a) Identifying Components
*   **i. Population:** All UCF students.
*   **ii. Sample:** The 150 UCF students who volunteered to participate in the initiative.
*   **iii. Parameter:** The true average weekly commute time of all UCF students ($\mu = 22$ minutes).
*   **iv. Statistic:** The average weekly commute time of the 150 students after the initiative ($\bar{x} = 18$ minutes).

### (b) Classification of Variables
*   **i. Weekly commute time:** Quantitative, Continuous.
*   **ii. Primary mode of transportation:** Qualitative.
*   **iii. Number of days a student commutes:** Quantitative, Discrete.
*   **iv. Whether a student uses the initiative:** Qualitative.

### (c) Levels of Measurement
*   **i. Weekly commute time:** Ratio.
*   **ii. Primary mode of transportation:** Nominal.
*   **iii. Number of days a student commutes:** Ratio.

### (d) Study Type
*   **Answer:** **Observational Study**.
*   **Justification:** The researcher did not randomly assign students to the carpooling initiative; instead, students volunteered (self-selection). The researcher is observing the outcomes of a group that chose to participate.

### (e) Causation
*   **Answer:** No.
*   **Explanation:** Because this is an observational study with volunteers, there may be confounding variables (e.g., highly motivated students). Without a control group and random assignment, the researcher cannot establish a cause-and-effect relationship.

### (f) Sampling Method
*   **i. Method:** Simple Random Sampling.
*   **ii. Why preferred:** It reduces selection bias (like volunteer bias) and ensures the sample is more representative of the entire population, allowing for better generalization of results.

---

## Question 2 Solutions

### (a) Five-Number Summary
*   **Given:** Data set: 40, 42, 45, 48, 50, 52, 55, 58, 62, 70, 85, 110, 145 ($n = 13$).
*   **Find:** Min, $Q_1$, Median, $Q_3$, Max.
*   **Calculation:**
    *   **i. Minimum:** **40**
    *   **iii. Median ($Q_2$):** The middle value of 13 items is the 7th item. **55**
    *   **ii. $Q_1$:** Median of the lower half (first 6 items: 40, 42, 45, 48, 50, 52).
        $Q_1 = \frac{45 + 48}{2} =$ **46.5**
    *   **iv. $Q_3$:** Median of the upper half (last 6 items: 58, 62, 70, 85, 110, 145).
        $Q_3 = \frac{70 + 85}{2} =$ **77.5**
    *   **v. Maximum:** **145**

### (b) Boxplot Construction
*   **Outlier Check:**
    *   $IQR = Q_3 - Q_1 = 77.5 - 46.5 = 31$
    *   $1.5 \times IQR = 1.5 \times 31 = 46.5$
    *   Upper Boundary $= Q_3 + 46.5 = 77.5 + 46.5 = 124$
    *   Lower Boundary $= Q_1 - 46.5 = 46.5 - 46.5 = 0$
    *   Since $145 > 124$, **145 is an outlier**.
*   **Boxplot Components:**
    *   Box from $46.5$ to $77.5$ with a line at $55$.
    *   Left whisker extends to $40$.
    *   Right whisker extends to $110$ (the largest value $\le 124$).
    *   An asterisk (*) or dot at $145$ to represent the outlier.

### (c) Distribution Shape
*   **Answer:** **Right-Skewed**.
*   **Justification:** The median (55) is closer to $Q_1$ (46.5) than to $Q_3$ (77.5), and there is a high-value outlier (145) on the right side, pulling the mean higher than the median.

---

## Question 3 Solutions

### (a) Basic Probabilities
*   **Given:** Total $N = 250$, Netflix $n(N) = 150$, Disney+ $n(D) = 100$, Both $n(N \cap D) = 60$.
*   **Calculation:**
    *   **i. $P(N) = \frac{150}{250} =$ **0.6000**
    *   **ii. $P(D) = \frac{100}{250} =$ **0.4000**
    *   **iii. $P(N \cap D) = \frac{60}{250} =$ **0.2400**

### (b) Probability of At Least One
*   **Formula:** $P(N \cup D) = P(N) + P(D) - P(N \cap D)$
*   **Substitution:** $0.6000 + 0.4000 - 0.2400$
*   **Final Answer:** **0.7600**

### (c) Conditional Probability
*   **Find:** $P(D|N)$
*   **Formula:** $P(D|N) = \frac{P(N \cap D)}{P(N)}$
*   **Substitution:** $\frac{0.2400}{0.6000}$
*   **Final Answer:** **0.4000**

### (d) Independence
*   **Check:** Does $P(D|N) = P(D)$?
*   **Comparison:** $0.4000 = 0.4000$.
*   **Answer:** **Yes, the events are independent**. Because the occurrence of $N$ does not change the probability of $D$ occurring.

### (e) Multiplication Rule (Without Replacement)
*   **Find:** $P(N_1 \cap N_2 \cap N_3)$
*   **Calculation:** $\frac{150}{250} \times \frac{149}{249} \times \frac{148}{248}$
*   **Substitution:** $0.6 \times 0.59839 \times 0.59677$
*   **Final Answer:** **0.2143**

---

## Question 4 Solutions

### (a) Probability Distribution of $X$
*   **Given:** 52 cards. Hearts (13), Aces not Heart (3), Others ($52 - 13 - 3 = 36$).
*   **Distribution Table:**
    *   $P(X = 5) = \frac{13}{52} = 0.2500$
    *   $P(X = 10) = \frac{3}{52} \approx 0.0577$
    *   $P(X = -4) = \frac{36}{52} \approx 0.6923$

### (b) Expected Value $E(X)$
*   **Formula:** $E(X) = \sum x \cdot P(x)$
*   **Substitution:** $5(0.25) + 10(0.0577) - 4(0.6923)$
*   **Calculation:** $1.25 + 0.577 - 2.7692$
*   **Final Answer:** **-$0.9422** (or -49/52 dollars)

### (c) Standard Deviation of $X$
*   **Formula:** $\sigma = \sqrt{E(X^2) - [E(X)]^2}$
*   **Calculation $E(X^2)$:** $5^2(0.25) + 10^2(0.0577) + (-4)^2(0.6923) = 6.25 + 5.77 + 11.0768 = 23.0968$
*   **Variance:** $23.0968 - (-0.9422)^2 = 23.0968 - 0.8877 = 22.2091$
*   **Standard Deviation:** $\sqrt{22.2091}$
*   **Final Answer:** **4.7127**

### (d) Binomial Probability $P(Y \ge 3)$
*   **Given:** $n = 12, p = 0.25, q = 0.75$.
*   **Find:** $P(Y \ge 3) = 1 - [P(0) + P(1) + P(2)]$
*   **Calculations:**
    *   $P(0) = (0.75)^{12} = 0.0317$
    *   $P(1) = 12 \times (0.25)^1 \times (0.75)^{11} = 0.1267$
    *   $P(2) = \binom{12}{2} \times (0.25)^2 \times (0.75)^{10} = 66 \times 0.0625 \times 0.0563 = 0.2323$
*   **Sum:** $1 - (0.0317 + 0.1267 + 0.2323) = 1 - 0.3907$
*   **Final Answer:** **0.6093**

### (e) Mean and SD of $Y$
*   **Mean:** $E(Y) = np = 12 \times 0.25 =$ **3.0**
*   **SD:** $\sigma_Y = \sqrt{npq} = \sqrt{12 \times 0.25 \times 0.75} = \sqrt{2.25} =$ **1.5**

---

## Question 5 Solutions

### (a) Sampling Distribution of $\bar{X}$
*   **Given:** $\mu = 15, \sigma = 4, n = 49$.
*   **Mean:** $\mu_{\bar{X}} = \mu =$ **15.0**
*   **SD:** $\sigma_{\bar{X}} = \frac{\sigma}{\sqrt{n}} = \frac{4}{\sqrt{49}} = \frac{4}{7} \approx$ **0.5714**

### (b) Probability $P(14 < \bar{X} < 16)$
*   **Z-scores:**
    *   $Z_1 = \frac{14 - 15}{0.5714} = -1.75$
    *   $Z_2 = \frac{16 - 15}{0.5714} = 1.75$
*   **Calculation:** $P(-1.75 < Z < 1.75) = P(Z < 1.75) - P(Z < -1.75)$
*   **Table Values:** $0.9599 - 0.0401$
*   **Final Answer:** **0.9198**

### (c) Normal Approximation Verification
*   **Check:** $np \ge 10$ and $n(1-p) \ge 10$
*   **Calculation:** $150 \times 0.40 = 60 \ge 10$; $150 \times 0.60 = 90 \ge 10$.
*   **Conclusion:** **Yes, the normal approximation can be used**.

### (d) Sampling Distribution of $\hat{p}$
*   **Mean:** $\mu_{\hat{p}} = p =$ **0.40**
*   **SD:** $\sigma_{\hat{p}} = \sqrt{\frac{p(1-p)}{n}} = \sqrt{\frac{0.4 \times 0.6}{150}} = \sqrt{0.0016} =$ **0.04**

### (e) Probability $P(\hat{p} > 0.45)$
*   **Z-score:** $Z = \frac{0.45 - 0.40}{0.04} = \frac{0.05}{0.04} = 1.25$
*   **Calculation:** $P(Z > 1.25) = 1 - P(Z < 1.25) = 1 - 0.8944$
*   **Final Answer:** **0.1056**

---

## Question 6 Solutions

### (a) Confidence Interval for $p$
*   **Given:** $n = 300, x = 210, \hat{p} = \frac{210}{300} = 0.70$.
*   **Critical Value ($Z_{0.05/2}$):** 1.96
*   **Standard Error:** $SE = \sqrt{\frac{0.7 \times 0.3}{300}} \approx 0.02646$
*   **Margin of Error:** $ME = 1.96 \times 0.02646 = 0.0519$
*   **Interval:** $0.70 \pm 0.0519$
*   **Final Answer:** **(0.6481, 0.7519)**

### (b) Interpretation
*   **Answer:** We are 95% confident that the true proportion of all UCF students who support extending library hours until 2:00 AM is between **64.81% and 75.19%**.
