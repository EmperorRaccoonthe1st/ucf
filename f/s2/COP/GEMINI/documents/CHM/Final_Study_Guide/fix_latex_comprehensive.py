import re

file_path = "exam4/intermediate_files/main.tex"
with open(file_path, "r") as f:
    content = f.read()

split_marker = r"\\section\{Stoichiometry\}"
parts = re.split(split_marker, content)

if len(parts) < 2:
    print("Could not find Stoichiometry section")
    exit(1)

header = parts[0]

rest_of_doc = r"""\section{Stoichiometry}

\subsection{Core Concepts}
Stoichiometry involves using the relationships between reactants and products in a balanced chemical equation to determine quantitative data.

\begin{itemize}
    \item \textbf{Mole Ratio}: Derived from the coefficients of a balanced equation; it is the "bridge" that allows conversion between different substances.
    \item \textbf{Limiting Reactant}: The reactant that is completely consumed first, limiting the amount of product formed.
    \item \textbf{Theoretical Yield}: The maximum amount of product that can be produced from a given amount of limiting reactant.
\end{itemize}

\begin{tcolorbox}[memorize, title=Reaction Efficiency *]
    \[ \text{Percent Yield} = \left( \frac{\text{Actual Yield}}{\text{Theoretical Yield}} \right) \times 100\% \]
\end{tcolorbox}

\subsection{Problem-Solving Skills}
\begin{enumerate}
    \item \textbf{Mass-to-Mass Stoichiometry}:
    \begin{itemize}
        \item $\text{Mass A} \xrightarrow{\div MM_A} \text{Moles A} \xrightarrow{\text{Mole Ratio}} \text{Moles B} \xrightarrow{\times MM_B} \text{Mass B}$
    \end{itemize}

    \item \textbf{Identifying the Limiting Reactant}:
    \begin{enumerate}[label=\alph*)]
        \item Convert the given amounts of all reactants to moles.
        \item Divide the moles of each reactant by its coefficient in the balanced equation.
        \item The reactant with the smallest resulting value is the \textbf{limiting reactant}.
    \end{enumerate}

    \item \textbf{Calculating Theoretical Yield}:
    \begin{itemize}
        \item Use the moles of the limiting reactant and the mole ratio from the balanced equation to find the moles (and then mass) of the desired product.
    \end{itemize}
\end{enumerate}

\newpage

\section{Solutions and Aqueous Reactions}

\subsection{Core Concepts}
Most chemical reactions occur in solution. Understanding concentration and the behavior of ions in water is critical.

\begin{itemize}
    \item \textbf{Molarity (M)}: A measure of concentration defined as moles of solute per liter of solution (\si{mol.L^{-1}}).
    \item \textbf{Electrolytes}: Substances that dissociate into ions in water (Strong = complete dissociation, Weak = partial).
    \item \textbf{Precipitation}: A reaction where two aqueous solutions form an insoluble solid product.
    \item \textbf{Oxidation States}: Bookkeeping for electrons to track redox processes.
\end{itemize}

\begin{tcolorbox}[memorize, title=Concentration and Dilution *]
    \[ M = \frac{n}{V} \quad \text{and} \quad M_1V_1 = M_2V_2 \]
\end{tcolorbox}

\subsection{Solubility Reference}
\begin{table}[h]
    \centering
    \caption{Solubility Guidelines for Ionic Compounds *}
    \begin{tabular}{ll}
        \toprule
        \textbf{Always Soluble} & \ce{NO3-}, \ce{C2H3O2-}, Group 1 (\ce{Li+}, \ce{Na+}, \ce{K+}), \ce{NH4+} \\
        \midrule
        \textbf{Generally Soluble} & \ce{Cl-}, \ce{Br-}, \ce{I-} (except \ce{Ag+}, \ce{Pb^{2+}}, \ce{Hg2^{2+}}) \\
                                  & \ce{SO4^{2-}} (except \ce{Ba^{2+}}, \ce{Sr^{2+}}, \ce{Ca^{2+}}, \ce{Pb^{2+}}, \ce{Ag+}) \\
        \midrule
        \textbf{Generally Insoluble} & \ce{S^{2-}}, \ce{OH-} (except Group 1, \ce{NH4+}; \ce{Ca^{2+}}, \ce{Sr^{2+}}, \ce{Ba^{2+}} are soluble) \\
                                    & \ce{CO3^{2-}}, \ce{PO4^{3-}} (except Group 1 and \ce{NH4+}) \\
        \bottomrule
    \end{tabular}
\end{table}

\subsection{Problem-Solving Skills}
\begin{enumerate}
    \item \textbf{Writing Net Ionic Equations}:
    \begin{enumerate}[label=\alph*)]
        \item Write the balanced molecular equation.
        \item Use solubility rules to identify precipitates (\ce{(s)}) and aqueous species (\ce{(aq)}).
        \item Write the complete ionic equation (dissociate all strong electrolytes).
        \item Cancel \textbf{spectator ions} (ions that appear identical on both sides).
    \end{enumerate}

    \item \textbf{Assigning Oxidation States}:
    \begin{itemize}
        \item Elements in standard state = 0; Monoatomic ions = charge.
        \item \ce{F} = -1; \ce{O} = -2 (usually); \ce{H} = +1 (with non-metals).
        \item The sum of oxidation states must equal the overall charge of the molecule/ion.
    \end{itemize}

    \item \textbf{Solution Stoichiometry \& Titration}:
    \begin{itemize}
        \item Use volume and molarity to find moles ($n = M \times V$).
        \item Apply stoichiometry from the balanced neutralization equation (e.g., \ce{HCl + NaOH -> NaCl + H2O}).
        \item At the equivalence point: $\text{moles H}^+ = \text{moles OH}^-$.
    \end{itemize}
\end{enumerate}

\newpage

\section{Heat and Enthalpy}

\subsection{Core Concepts}
\begin{itemize}
    \item \textbf{Calorimetry}: The measurement of heat flow into or out of a system during a chemical or physical process.
    \item \textbf{Conservation of Energy}: In an insulated system, heat lost by one component is gained by another: $-q_{\text{lost}} = q_{\text{gained}}$.
    \item \textbf{Standard Enthalpy of Formation ($\Delta H_f^\circ$)}: The change in enthalpy when 1 mole of a substance is formed from its elements in their standard states. Note: $\Delta H_f^\circ = 0$ for any element in its most stable form (e.g., \ce{O2(g)}, \ce{C(graphite)}).
    \item \textbf{Hess's Law}: If a reaction is carried out in a series of steps, $\Delta H$ for the overall reaction equals the sum of the enthalpy changes for the individual steps.
\end{itemize}

\subsection{Calorimetry}
\begin{tcolorbox}[provided, title=Specific Heat Equation (Provided)]
    \[ q = m c_s \Delta T \]
\end{tcolorbox}

\subsection{Reaction Enthalpy Calculations}
\begin{tcolorbox}[memorize, title=Enthalpy Calculations *]
    \textbf{From Heats of Formation}:
    \[ \Delta H_{\text{rxn}}^\circ = \sum n\Delta H_f^\circ(\text{products}) - \sum m\Delta H_f^\circ(\text{reactants}) \]
    \vspace{0.2em}
    \textbf{From Bond Energies}:
    \[ \Delta H_{\text{rxn}}^\circ = \sum (\text{bonds broken}) - \sum (\text{bonds formed}) \]
\end{tcolorbox}
\textbf{Crucial Distinction}: Formation uses (Products - Reactants), while Bond Energy uses (Reactants/Broken - Products/Formed).

\subsection{Problem-Solving Skills}
\begin{enumerate}
    \item \textbf{Calculating Reaction Enthalpy}:
        \begin{itemize}
            \item Identify $\Delta H_f^\circ$ for all species. Pure elements in standard states are \SI{0}{\kilo\joule\per\mole}.
            \item Multiply each value by its stoichiometric coefficient.
            \item Apply: $\text{Products} - \text{Reactants}$.
        \end{itemize}
    \item \textbf{Applying Hess's Law}:
        \begin{itemize}
            \item If you reverse a reaction, flip the sign of $\Delta H$.
            \item If you multiply coefficients by a factor $n$, multiply $\Delta H$ by $n$.
            \item Sum the modified $\Delta H$ values to find the target enthalpy.
        \end{itemize}
\end{enumerate}

\newpage

\section{Structure and Bonding}

\subsection{Core Concepts}
\begin{itemize}
    \item \textbf{Formal Charge}: Used to determine the most plausible Lewis structure. The best structure minimizes formal charges and places negative charges on the most electronegative atoms.
    \item \textbf{Lattice Energy}: The energy required to separate 1 mole of an ionic solid into gaseous ions. It increases with increasing ion charge and decreasing ion size.
    \item \textbf{VSEPR Theory}: Predicts molecular shape based on the repulsion between electron domains (bonding pairs and lone pairs).
    \item \textbf{Hybridization}: The mixing of atomic orbitals to form new hybrid orbitals (e.g., $sp, sp^2, sp^3$) suitable for bonding.
\end{itemize}

\subsection{Lattice Energy and Formal Charge}
\begin{tcolorbox}[memorize, title=Coulomb's Law *]
    \[ E_{\text{lattice}} \propto \frac{Q_1 Q_2}{d} \]
\end{tcolorbox}

\begin{tcolorbox}[memorize, title=Formal Charge *]
    \[ FC = (\text{Valence } e^-) - (\text{Non-bonding } e^-) - \frac{1}{2}(\text{Bonding } e^-) \]
\end{tcolorbox}

\subsection{Molecular Geometry Example: Tetrahedral}
Centrally bonded atoms with four electron domains (e.g., \ce{CH4}) adopt a tetrahedral geometry with bond angles of approximately \SI{109.5}{\degree}.

\begin{center}
    \chemfig{C(-[2]H)(<:[5]H)(<[6]H)(-[0]H)}
    \quad
    \textit{Tetrahedral Geometry (\ce{CH4})}
\end{center}

\subsection{Problem-Solving Skills}
\begin{enumerate}
    \item \textbf{Determining Hybridization}: Count electron domains (lone pairs + bonding regions).
        \begin{itemize}
            \item 2 domains: $sp$ (Linear)
            \item 3 domains: $sp^2$ (Trigonal Planar)
            \item 4 domains: $sp^3$ (Tetrahedral)
        \end{itemize}
    \item \textbf{Bond Counting}: Every single bond is 1 $\sigma$. Double bonds consist of 1 $\sigma$ and 1 $\pi$. Triple bonds consist of 1 $\sigma$ and 2 $\pi$.
\end{enumerate}

\newpage

\section{States of Matter}

\subsection{Core Concepts}
\begin{itemize}
    \item \textbf{Ideal Gas Law}: Relates pressure, volume, temperature, and moles. Assumes gas particles have no volume and no IMFs.
    \item \textbf{Kinetic Molecular Theory (KMT)}: Gas particles are in constant random motion. Temperature is a measure of average kinetic energy.
    \item \textbf{Intermolecular Forces (IMFs)}:
        \begin{itemize}
            \item \textbf{London Dispersion}: Present in all molecules; strength increases with polarizability (larger electron clouds).
            \item \textbf{Dipole-Dipole}: Between polar molecules.
            \item \textbf{Hydrogen Bonding}: Strong dipole-dipole interaction involving H bonded to N, O, or F.
        \end{itemize}
\end{itemize}

\subsection{Gas Laws and Constants}
\begin{tcolorbox}[provided, title=Gas Laws and Constants (Provided)]
    \textbf{Constants}:
    \[ R = \SI{0.0821}{\liter.atm.mol^{-1}.K^{-1}} \]
    \[ 1 \text{ atm} = 760 \text{ mmHg} = 760 \text{ Torr} \]
    \vspace{0.5em}
    \textbf{Laws}:
    \[ PV = nRT \quad \text{and} \quad \frac{P_1V_1}{n_1T_1} = \frac{P_2V_2}{n_2T_2} \]
    \vspace{0.5em}
    \textbf{Graham's Law of Effusion}:
    \[ \frac{\text{rate}_1}{\text{rate}_2} = \sqrt{\frac{M_2}{M_1}} \]
\end{tcolorbox}

\subsection{Gas Density}
\begin{tcolorbox}[memorize, title=Gas Density *]
    \[ d = \frac{PM}{RT} \]
\end{tcolorbox}

\subsection{Maxwell-Boltzmann Distribution}
The distribution of molecular speeds changes with temperature. At higher temperatures, the peak shifts right (higher average speed) and flattens (wider distribution of speeds).

\begin{center}
\begin{tikzpicture}
\begin{axis}[
    axis lines = left,
    xlabel = {Molecular Speed ($v$)},
    ylabel = {Relative Number of Molecules},
    ticks = none,
    xmin = 0, xmax = 10,
    ymin = 0, ymax = 1,
    width = 8cm, height = 5cm,
    legend pos = north east
]
% Low Temperature (T1)
\addplot [domain=0:10, samples=100, thick, blue] {4*x^2*exp(-x^2)};
\addlegendentry{$T_{\text{low}}$}
% High Temperature (T2)
\addplot [domain=0:10, samples=100, thick, red] {0.8*x^2*exp(-0.2*x^2)};
\addlegendentry{$T_{\text{high}}$}
\end{axis}
\end{tikzpicture}
\end{center}

\subsection{Problem-Solving Skills}
\begin{enumerate}
    \item \textbf{Gas Law Calculations}: Always convert temperature to \si{\kelvin} ($T_K = T_C + 273.15$). Ensure units match the $R$ constant.
    \item \textbf{Predicting Physical Properties}: Stronger IMFs result in higher boiling points, higher melting points, and lower vapor pressures.
\end{enumerate}

\newpage

\section*{Addendum: Exam Formula \& Constant Reference}

\subsection*{Provided Information}
\begin{itemize}
    \item \textbf{Temperature}: $T_{\si{\kelvin}} = T_{^\circ\text{C}} + 273.15$
    \item \textbf{Avogadro Constant}: $N_A = \num{6.022e23} \si{mol^{-1}}$
    \item \textbf{Gas Constant}: $R = \SI{0.0821}{\liter.atm.mol^{-1}.K^{-1}}$
    \item \textbf{Pressure}: $1 \text{ atm} = \SI{760}{mmHg} = \SI{760}{Torr}$
    \item \textbf{Ideal Gas Law}: $PV = nRT$
    \item \textbf{Combined Gas Law}: $\frac{P_1V_1}{n_1T_1} = \frac{P_2V_2}{n_2T_2}$
    \item \textbf{Graham's Law}: $\frac{\text{rate}_1}{\text{rate}_2} = \sqrt{\frac{M_2}{M_1}}$
    \item \textbf{Specific Heat}: $q = m c_s \Delta T$
\end{itemize}

\subsection*{Information to Memorize *}
\begin{itemize}
    \item \textbf{Atomic Mass}: $\sum (\text{mass} \times \text{fraction abundance})$
    \item \textbf{Light}: $c = \lambda \nu$ and $E = h\nu = hc/\lambda$
    \item \textbf{Rydberg}: $\Delta E = -2.18 \times 10^{-18} \si{J} (1/n_f^2 - 1/n_i^2)$
    \item \textbf{Molarity}: $M = n/V$
    \item \textbf{Enthalpy (Formation)}: $\sum \Delta H_f^\circ(\text{prod}) - \sum \Delta H_f^\circ(\text{react})$
    \item \textbf{Enthalpy (Bonds)}: $\sum (\text{broken}) - \sum (\text{formed})$
    \item \textbf{Lattice Energy}: $E \propto Q_1Q_2/d$
    \item \textbf{Solubility}: (See Table in Chapter 6)
\end{itemize}

\end{document}
"""

with open(file_path, "w") as f:
    f.write(header + rest_of_doc)
