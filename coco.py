import streamlit as st
import pandas as pd
import seaborn as sns
from my_styles import * 


# st.write(df.columns)

def main():
    df = pd.read_csv('coco.csv')

    st.set_option('deprecation.showPyplotGlobalUse', False)

    st.write("## COCONUT Database")
    st.write("Natural Products Online is an open-source platform for storing, searching, and analyzing Natural Products (NPs). It currently features COCONUT, the COllection of Open Natural ProdUcts, which is one of the largest and highly annotated resources for NPs available for free and unrestricted use.")
    c1, c2 = st.columns((21,13))
    c2.write('#### Chemical synthesis')
    c2.write("The difficulty of synthesizing a chemical compound is determined by two key factors: the number of spiro atoms and the fraction of sp3 carbon atoms. These parameters influence the synthesis process by affecting the molecule's stability, reactivity, and other properties. The greater the number of spiro atoms and the higher the fraction of sp3 carbon atoms, the more challenging it becomes to synthesize the compound. It is important for chemical engineers and synthetic chemists to consider these factors in order to optimize the synthesis process and produce high-quality, stable compounds.")

    c1.write("#### fsp3 VS number of Spiro Atoms")
    sns.scatterplot(x='fsp3', y='numberSpiroAtoms', data=df, hue='lipinskiRuleOf5Failures')
    c1.pyplot()


    col1, col2 = st.columns(2)
    col1.write("Boxplot of xlog and lipinski Rule Of 5 Failures")
    sns.boxplot(y='xlogp', 
            x='lipinskiRuleOf5Failures', 
            data=df, 
            showfliers=False,
            )
    col1.pyplot()

    col2.write("Boxplot of molecular weight and lipinski Rule Of 5 Failures")

    sns.boxplot(y='molecular_weight', 
            x='lipinskiRuleOf5Failures', 
            data=df, 
            showfliers=False,
            )
    col2.pyplot()
    st.write("""
The drug discovery process is greatly influenced by several parameters, including XlogP, molecular weight, and Lipinski's Rule of 5.

XlogP is a measure of a molecule's hydrophobicity, which is an important factor in determining its pharmacokinetics and solubility. Compounds with high XlogP values are typically more lipophilic and have slower clearance rates, making them more suitable for oral administration. On the other hand, compounds with low XlogP values are more hydrophilic and may have faster clearance rates, making them better suited for intravenous administration.

Molecular weight is another important factor in drug discovery as it affects the drug's pharmacokinetics, bioavailability, and distribution. In general, smaller compounds tend to be more bioavailable and have a higher solubility compared to larger compounds, making them more attractive for drug discovery.

Lipinski's Rule of 5, named after medicinal chemist Christopher Lipinski, is a guideline that suggests that drug-like compounds should have a molecular weight of less than 500 daltons, an XlogP value less than 5, and no more than 5 hydrogen bond donors and 10 hydrogen bond acceptors. Compounds that violate one or more of these criteria are more likely to have poor pharmacokinetics and are therefore less likely to be successful as drugs.

In conclusion, XlogP, molecular weight, and Lipinski's Rule of 5 are crucial parameters in drug discovery, as they influence the pharmacokinetics, solubility, and bioavailability of a molecule, and can greatly affect its potential as a drug candidate.
        """)


if __name__=="__main__":
    main()
    st.markdown(footer,unsafe_allow_html=True)
