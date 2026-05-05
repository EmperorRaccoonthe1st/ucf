# Draft Answers for STA 2023 Final Exam Practice

## Question 1(a)
- **Given:** Population of UCF students, true average stress $\mu = 65$, sample size $n = 200$, sample initial mean $\bar{x}_{before} = 66$, sample final mean $\bar{x}_{after} = 54$.
- **Find:** Identify the Population, Sample, Parameter, and Statistic.
- **Formula Selection:** N/A (Definitional)
- **Substitution:** N/A
- **Calculation:** N/A
- **Rounding:** N/A
- **Final Answer:** 
  i. **Population: All UCF students**
  ii. **Sample: The 200 UCF students who volunteered**
  iii. **Parameter: $\mu = 65$ (The true average stress level of all UCF students)**
  iv. **Statistic: $\bar{x}_{before} = 66$ and $\bar{x}_{after} = 54$ (The average stress levels of the sample)**

## Question 1(b)
- **Given:** Four variables: Stress score (0-100), Student major, Hours of sleep, Program participation (Yes/No).
- **Find:** Classify as qualitative or quantitative, and discrete or continuous if quantitative.
- **Formula Selection:** N/A
- **Substitution:** N/A
- **Calculation:** N/A
- **Rounding:** N/A
- **Final Answer:** 
  i. **Quantitative, Discrete**
  ii. **Qualitative**
  iii. **Quantitative, Continuous**
  iv. **Qualitative**

## Question 1(c)
- **Given:** Variables from (b).
- **Find:** Level of measurement for Stress score, Student major, Hours of sleep.
- **Formula Selection:** N/A
- **Substitution:** N/A
- **Calculation:** N/A
- **Rounding:** N/A
- **Final Answer:** 
  i. **Interval**
  ii. **Nominal**
  iii. **Ratio**

## Question 1(d)
- **Given:** The researcher "selects 200 UCF students who volunteer to participate in the program."
- **Find:** Observational study or designed experiment? Justify.
- **Formula Selection:** N/A
- **Substitution:** N/A
- **Calculation:** N/A
- **Rounding:** N/A
- **Final Answer:** **Designed experiment. The researcher is actively applying a treatment (the wellness program) to the subjects to measure its effect on their stress levels, rather than just observing them without interference.**

## Question 1(e)
- **Given:** The study design and the reduction in stress levels.
- **Find:** Can the researcher conclude causation? Explain.
- **Formula Selection:** N/A
- **Substitution:** N/A
- **Calculation:** N/A
- **Rounding:** N/A
- **Final Answer:** **No. Because the participants were volunteers (not randomly assigned to a treatment and control group), there may be confounding variables (such as motivation to reduce stress) that caused the reduction. Without randomization and a control group, causation cannot be definitively established.**

## Question 1(f)
- **Given:** Random selection from all UCF students using a student ID list.
- **Find:** Type of sampling method and why it is preferred.
- **Formula Selection:** N/A
- **Substitution:** N/A
- **Calculation:** N/A
- **Rounding:** N/A
- **Final Answer:** 
  i. **Simple random sampling**
  ii. **It removes selection bias and ensures the sample is more representative of the entire population, unlike a volunteer sample which is prone to volunteer bias.**

## Question 2(a)
- **Given:** Data set: $45, 52, 60, 63, 67, 70, 72, 75, 78, 85, 90, 95, 120$ ($n=13$).
- **Find:** Five-number summary (Minimum, $Q_1$, Median $Q_2$, $Q_3$, Maximum).
- **Formula Selection:** Median of ordered data, $Q_1$ is median of lower half, $Q_3$ is median of upper half.
- **Substitution:** 
  - Lower half: $45, 52, 60, 63, 67, 70$
  - Upper half: $75, 78, 85, 90, 95, 120$
- **Calculation:** 
  - Median $Q_2$ = 7th value = $72$
  - $Q_1 = (60 + 63) / 2 = 61.5$
  - $Q_3 = (85 + 90) / 2 = 87.5$
- **Rounding:** None
- **Final Answer:** 
  i. **Minimum = 45**
  ii. **$Q_1$ = 61.5**
  iii. **Median $Q_2$ = 72**
  iv. **$Q_3$ = 87.5**
  v. **Maximum = 120**

## Question 2(b)
- **Given:** Five-number summary: $45, 61.5, 72, 87.5, 120$.
- **Find:** Construct a boxplot and clearly label $Q_1$, median, $Q_3$, whiskers, and outliers.
- **Formula Selection:** $IQR = Q_3 - Q_1$, Lower Fence $= Q_1 - 1.5 \times IQR$, Upper Fence $= Q_3 + 1.5 \times IQR$.
- **Substitution:** 
  - $IQR = 87.5 - 61.5$
  - Lower Fence $= 61.5 - 1.5(26)$
  - Upper Fence $= 87.5 + 1.5(26)$
- **Calculation:** 
  - $IQR = 26$
  - Lower Fence $= 61.5 - 39 = 22.5$
  - Upper Fence $= 87.5 + 39 = 126.5$
  - Outliers: Any value $< 22.5$ or $> 126.5$. Minimum is 45 and Maximum is 120, so no outliers.
- **Rounding:** None
- **Final Answer:** **A boxplot drawn with a box extending from $Q_1 = 61.5$ to $Q_3 = 87.5$, with a vertical line inside at the Median = $72$. The left whisker extends to the Minimum = $45$, and the right whisker extends to the Maximum = $120$. Outliers: None.**

## Question 2(c)
- **Given:** Boxplot metrics: $Q_1 = 61.5$, Median $= 72$, $Q_3 = 87.5$.
- **Find:** Describe the shape of the distribution and justify.
- **Formula Selection:** Compare $(Q_3 - \text{Median})$ to $(\text{Median} - Q_1)$ and $(\text{Maximum} - \text{Median})$ to $(\text{Median} - \text{Minimum})$.
- **Substitution:** 
  - $Q_3 - \text{Median} = 87.5 - 72 = 15.5$
  - $\text{Median} - Q_1 = 72 - 61.5 = 10.5$
- **Calculation:** The right side of the box (15.5) is longer than the left side of the box (10.5). Also, the right whisker ($120 - 72 = 48$) is longer than the left whisker ($72 - 45 = 27$).
- **Rounding:** None
- **Final Answer:** **Right-skewed. The distance from the median to $Q_3$ is greater than the distance from $Q_1$ to the median, and the right whisker is longer than the left whisker, indicating a longer tail on the right side.**

## Question 3(a)
- **Given:** $N = 200$ students, $n(L) = 120$ own laptop, $n(T) = 80$ own tablet, $n(L \cap T) = 50$ own both.
- **Find:** Probability student owns a laptop, owns a tablet, owns both.
- **Formula Selection:** $P(A) = n(A) / N$
- **Substitution:** $P(L) = 120 / 200$, $P(T) = 80 / 200$, $P(L \cap T) = 50 / 200$
- **Calculation:** $120/200 = 0.6$, $80/200 = 0.4$, $50/200 = 0.25$
- **Rounding:** Four decimal places.
- **Final Answer:** 
  i. **0.6000**
  ii. **0.4000**
  iii. **0.2500**

## Question 3(b)
- **Given:** $P(L) = 0.6000$, $P(T) = 0.4000$, $P(L \cap T) = 0.2500$
- **Find:** Probability student owns at least one device ($P(L \cup T)$).
- **Formula Selection:** $P(L \cup T) = P(L) + P(T) - P(L \cap T)$
- **Substitution:** $P(L \cup T) = 0.6000 + 0.4000 - 0.2500$
- **Calculation:** $1.0000 - 0.2500 = 0.7500$
- **Rounding:** Four decimal places.
- **Final Answer:** **0.7500**

## Question 3(c)
- **Given:** $P(L) = 0.6000$, $P(L \cap T) = 0.2500$
- **Find:** Probability owns a tablet given owns a laptop ($P(T | L)$).
- **Formula Selection:** $P(T | L) = \frac{P(T \cap L)}{P(L)}$
- **Substitution:** $P(T | L) = \frac{0.2500}{0.6000}$
- **Calculation:** $0.25 / 0.6 = 5 / 12 = 0.41666...$
- **Rounding:** Four decimal places.
- **Final Answer:** **0.4167**

## Question 3(d)
- **Given:** $P(L) = 0.6000$, $P(T) = 0.4000$, $P(L \cap T) = 0.2500$
- **Find:** Are the events independent? Justify.
- **Formula Selection:** Two events are independent if $P(L) \times P(T) = P(L \cap T)$
- **Substitution:** $0.6000 \times 0.4000 \stackrel{?}{=} 0.2500$
- **Calculation:** $0.6000 \times 0.4000 = 0.2400$. Since $0.2400 \neq 0.2500$, they are not independent.
- **Rounding:** Four decimal places.
- **Final Answer:** **No, the events are not independent because $P(L) \times P(T) = 0.2400$, which is not equal to $P(L \cap T) = 0.2500$.**

## Question 3(e)
- **Given:** Total $N = 200$, total laptops $n(L) = 120$. 3 selected without replacement.
- **Find:** Probability all 3 own a laptop.
- **Formula Selection:** $P(L_1 \cap L_2 \cap L_3) = P(L_1) \times P(L_2 | L_1) \times P(L_3 | L_1 \cap L_2)$
- **Substitution:** $P(L_1 \cap L_2 \cap L_3) = \left(\frac{120}{200}\right) \times \left(\frac{119}{199}\right) \times \left(\frac{118}{198}\right)$
- **Calculation:** $\frac{120 \times 119 \times 118}{200 \times 199 \times 198} = \frac{1685040}{7880400} = 0.213826...$
- **Rounding:** Four decimal places.
- **Final Answer:** **0.2138**

## Question 4(a)
- **Given:** Die rolled once. $X$ = money won. Outcomes: 1 or 2 (lose \$2), 3, 4, or 5 (win \$1), 6 (win \$5).
- **Find:** Probability distribution of $X$.
- **Formula Selection:** $P(X = x) = \frac{\text{number of favorable outcomes}}{\text{total outcomes}}$
- **Substitution:** 
  - $P(X = -2) = 2/6 = 1/3$
  - $P(X = 1) = 3/6 = 1/2$
  - $P(X = 5) = 1/6$
- **Calculation:** N/A
- **Rounding:** Four decimal places for probabilities.
- **Final Answer:** 
  **$x = -2$, $P(X = -2) = 0.3333$**
  **$x = 1$, $P(X = 1) = 0.5000$**
  **$x = 5$, $P(X = 5) = 0.1667$**

## Question 4(b)
- **Given:** Probability distribution from (a).
- **Find:** Expected value, $E(X)$.
- **Formula Selection:** $E(X) = \sum [x \times P(X=x)]$
- **Substitution:** $E(X) = (-2)(2/6) + (1)(3/6) + (5)(1/6)$
- **Calculation:** $-4/6 + 3/6 + 5/6 = 4/6 = 2/3 = 0.66666...$
- **Rounding:** Four decimal places.
- **Final Answer:** **$0.6667**

## Question 4(c)
- **Given:** Probability distribution from (a), $E(X) = 2/3$.
- **Find:** Standard deviation of $X$.
- **Formula Selection:** $\sigma = \sqrt{\sum [x^2 \times P(x)] - [E(X)]^2}$
- **Substitution:** $E(X^2) = (-2)^2(2/6) + (1)^2(3/6) + (5)^2(1/6)$
  $\sigma = \sqrt{E(X^2) - (2/3)^2}$
- **Calculation:** $E(X^2) = 4(2/6) + 1(3/6) + 25(1/6) = 8/6 + 3/6 + 25/6 = 36/6 = 6$. 
  Variance = $6 - 4/9 = 54/9 - 4/9 = 50/9 = 5.5555...$
  $\sigma = \sqrt{50/9} = \sqrt{5.5555...} = 2.35702...$
- **Rounding:** Four decimal places.
- **Final Answer:** **2.3570**

## Question 4(d)
- **Given:** Game played $n=10$ times. $Y$ = number of times player wins \$1 (i.e., rolls 3, 4, 5). $p = 3/6 = 0.5$.
- **Find:** Probability player wins \$1 at least 3 times, $P(Y \ge 3)$.
- **Formula Selection:** Binomial Probability: $P(Y \ge 3) = 1 - P(Y \le 2) = 1 - [P(Y=0) + P(Y=1) + P(Y=2)]$, where $P(Y=y) = \binom{n}{y} p^y (1-p)^{n-y}$
- **Substitution:** $P(Y \ge 3) = 1 - [\binom{10}{0}(0.5)^{10} + \binom{10}{1}(0.5)^{10} + \binom{10}{2}(0.5)^{10}]$
- **Calculation:** 
  $P(Y=0) = 1 \times 0.0009765 = 0.0009765$
  $P(Y=1) = 10 \times 0.0009765 = 0.0097656$
  $P(Y=2) = 45 \times 0.0009765 = 0.0439453$
  Sum = $0.0546875$
  $1 - 0.0546875 = 0.9453125$
- **Rounding:** Four decimal places.
- **Final Answer:** **0.9453**

## Question 4(e)
- **Given:** Binomial distribution, $n = 10$, $p = 0.5$.
- **Find:** Mean and standard deviation of $Y$.
- **Formula Selection:** $\mu_Y = n \times p$, $\sigma_Y = \sqrt{n \times p \times (1-p)}$
- **Substitution:** $\mu_Y = 10 \times 0.5$, $\sigma_Y = \sqrt{10 \times 0.5 \times 0.5}$
- **Calculation:** $\mu_Y = 5$, $\sigma_Y = \sqrt{2.5} = 1.58113...$
- **Rounding:** Four decimal places.
- **Final Answer:** **Mean = 5, Standard Deviation = 1.5811**

## Question 5(a)
- **Given:** Population mean $\mu = 180$, Population standard dev $\sigma = 20$, Sample size $n = 64$.
- **Find:** Mean ($\mu_{\bar{x}}$) and standard deviation ($\sigma_{\bar{x}}$) of the sampling distribution of $\bar{x}$.
- **Formula Selection:** $\mu_{\bar{x}} = \mu$, $\sigma_{\bar{x}} = \frac{\sigma}{\sqrt{n}}$
- **Substitution:** $\mu_{\bar{x}} = 180$, $\sigma_{\bar{x}} = \frac{20}{\sqrt{64}}$
- **Calculation:** $\sigma_{\bar{x}} = 20 / 8 = 2.5$
- **Rounding:** None needed.
- **Final Answer:** **Mean = 180, Standard Deviation = 2.5**

## Question 5(b)
- **Given:** $\mu_{\bar{x}} = 180$, $\sigma_{\bar{x}} = 2.5$.
- **Find:** $P(175 < \bar{x} < 185)$
- **Formula Selection:** $Z = \frac{\bar{x} - \mu_{\bar{x}}}{\sigma_{\bar{x}}}$
- **Substitution:** $Z_1 = \frac{175 - 180}{2.5}$, $Z_2 = \frac{185 - 180}{2.5}$
- **Calculation:** $Z_1 = -5 / 2.5 = -2.00$, $Z_2 = 5 / 2.5 = 2.00$.
  $P(-2.00 < Z < 2.00) = P(Z < 2.00) - P(Z < -2.00) = 0.9772 - 0.0228 = 0.9544$
- **Rounding:** Four decimal places.
- **Final Answer:** **0.9544**

## Question 5(c)
- **Given:** $p = 0.30$, $n = 100$.
- **Find:** Verify whether the normal approximation can be used for $\hat{p}$.
- **Formula Selection:** Check if $n \times p \ge 10$ and $n \times (1-p) \ge 10$.
- **Substitution:** $100 \times 0.30 \ge 10$ and $100 \times 0.70 \ge 10$.
- **Calculation:** $30 \ge 10$ and $70 \ge 10$. Both conditions are satisfied.
- **Rounding:** N/A
- **Final Answer:** **Yes, the normal approximation can be used because both $n \times p = 30$ and $n \times (1-p) = 70$ are greater than or equal to 10.**

## Question 5(d)
- **Given:** $p = 0.30$, $n = 100$.
- **Find:** Mean ($\mu_{\hat{p}}$) and standard deviation ($\sigma_{\hat{p}}$) of the sampling distribution of $\hat{p}$.
- **Formula Selection:** $\mu_{\hat{p}} = p$, $\sigma_{\hat{p}} = \sqrt{\frac{p(1-p)}{n}}$
- **Substitution:** $\mu_{\hat{p}} = 0.30$, $\sigma_{\hat{p}} = \sqrt{\frac{0.30(0.70)}{100}}$
- **Calculation:** $\sigma_{\hat{p}} = \sqrt{0.21 / 100} = \sqrt{0.0021} = 0.045825...$
- **Rounding:** Four decimal places.
- **Final Answer:** **Mean = 0.3000, Standard Deviation = 0.0458**

## Question 5(e)
- **Given:** $\mu_{\hat{p}} = 0.30$, $\sigma_{\hat{p}} = 0.0458$ (using unrounded $0.0458257...$ for calculation).
- **Find:** $P(\hat{p} > 0.35)$
- **Formula Selection:** $Z = \frac{\hat{p} - \mu_{\hat{p}}}{\sigma_{\hat{p}}}$
- **Substitution:** $Z = \frac{0.35 - 0.30}{0.0458257...}$
- **Calculation:** $Z = 0.05 / 0.0458257... \approx 1.09$.
  $P(Z > 1.09) = 1 - P(Z < 1.09) = 1 - 0.8621 = 0.1379$.
- **Rounding:** Four decimal places.
- **Final Answer:** **0.1379**

## Question 6(a)
- **Given:** Confidence level = 95%, Sample size $n = 250$, Number of successes $x = 165$.
- **Find:** Construct a 95% confidence interval for the true proportion.
- **Formula Selection:** $\hat{p} \pm z_{\alpha/2} \sqrt{\frac{\hat{p}(1-\hat{p})}{n}}$
- **Substitution:** $\hat{p} = 165 / 250 = 0.66$. For 95% CI, $z_{\alpha/2} = 1.96$.
  $0.66 \pm 1.96 \sqrt{\frac{0.66(1 - 0.66)}{250}}$
- **Calculation:** $0.66 \pm 1.96 \sqrt{\frac{0.66(0.34)}{250}} = 0.66 \pm 1.96 \sqrt{0.0008976} = 0.66 \pm 1.96(0.02996) = 0.66 \pm 0.0587$.
  Lower bound = $0.66 - 0.0587 = 0.6013$.
  Upper bound = $0.66 + 0.0587 = 0.7187$.
- **Rounding:** Four decimal places for the intermediate and final bounds.
- **Final Answer:** **(0.6013, 0.7187) or 60.13% to 71.87%**

## Question 6(b)
- **Given:** Confidence interval (0.6013, 0.7187).
- **Find:** Interpret the confidence interval in context.
- **Formula Selection:** "We are C% confident that the true parameter lies between [lower] and [upper]."
- **Substitution:** C = 95, parameter = proportion of all students who support having flu vaccination clinics, lower = 60.13%, upper = 71.87%.
- **Calculation:** N/A
- **Rounding:** N/A
- **Final Answer:** **We are 95% confident that the true proportion of all students who support having flu vaccination clinics on campus every semester lies between 60.13% and 71.87%.**
