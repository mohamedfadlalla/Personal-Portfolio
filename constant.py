import pandas as pd
import graphviz as graphviz

edu = [['B.Tech','CSE','2020','IIIT Jabalpur','8.1 CGPA'],['12th','Science','2016','Bhavan\'s KDKVM', '94.2%'],['10th','-','2012','Bhavan\'s KDKVM','10 CGPA']]

info = {'name':'Mohamed Fadlalla', 
'Brief':'''
As a recent graduate with a strong background in coding and data science, I have a track record of working with large-scale data sets and using my skills to drive meaningful insights. With over three years of experience coding in Python and more than two years in data science, I am comfortable manipulating big data and have successfully completed a number of projects, including building a ResearchGate scrapper, conducting a Pocketome analysis with 1 million records, and performing Coconut structure minimization. My expertise in big data and my passion for solving complex problems make me an ideal candidate for machine learning engineering roles.
''',
'photo':{'path':'abc.jpg','width':150}, 
'Mobile':'0129438898',
'Email':'mohamedbadrelmaarif@gmail.com',
'City':'Khartoum, Sudan',
'edu':pd.DataFrame(edu,columns=['Qualification','Stream','Year','Institute','Score']),
'ds-skills':['Web Scraping',
        'SQLite',
        ' google colab',
        'Pandas',
        ' GIT and GitHub',
        'streamlit',
        'Data Visuliaztaion'],
'research-skills':['Molecular docking',
        'Molecular Dynamics',
        'Biopython',
        'AutoDock 4.2',
        'AutoDock Vina',
        'Protein Modelling',
        'Google Scholar',
        'Scientific writing (scientific papers publication)',
        'UCSF Chimera'],
'Essential Skills':['Google Suite',
        'Presentation Skill',
        'NOTION',
        'Time Management',]}

paper_info = {'name':['Molecular Docking as a Potential Approach in Repurposing Drugs Against COVID-19: a Systematic Review and Novel Pharmacophore Models','COVID19 Approved Drug Repurposing: Pocket Similarity Approach'],
        'publication':['Springer','chemrxiv'],
        'journal':['Current Pharmacology Reports','chemrxiv'],
        'year':['2022','2020'],
        'role':['Author','Author'],
        'Summary':[
        '''
        Drug repurposing explores previously approved drugs of known safety and pharmacokinetics profile for possible new effects, reducing the cost, time, and predicting prospective side effects and drug interactions. COVID-19 virulent machinery appeared similar to other viruses, making antiviral agents widely repurposed in pursuit for curative candidates. Our main protease pharmacophoric study revealed multiple features and could be a probable starting point for upcoming research.
        ''',
        '''
        SARS CoV 2 has spread worldwide and caused a major outbreak of coronavirus disease 2019 (COVID-19). To date, no licensed drug or a vaccine is available against COVID19.

Starting from all of the resolved SARS CoV2 crystal structures, this study aims to find inhibitors for all of the SARS CoV2 proteins. To achieve this, I used PocketMatch to test the similarity of approved drugs binding sites against all of the binding sites found on SARS CoV 2 proteins. After that docking was used to confirm the results.

I found drugs that inhibit the main protease, Nsp12 and Nsp3. The discovered drugs are either in clinical trials (Sildenafil, Lopinavir, Ritonavir) or have in vitro antiviral activity (Nelfinavir, Indinavir, Amprenavir, depiqulinum , Gemcitabine, Raltitrexed, Aprepitant, montelukast, Ouabain, Raloxifene) whether against SARS CoV 2 or other viruses. In addition to this, further analysis of pockets revealed a steroidal pocket that might open the door to hypotheses on why the mortality of men is higher than women.

Many of the in silico repurposing studies test binding of the compound to the target using docking. The significance of this study adds to the similarity between the drug binding site and the target binding site. This takes into consideration the dynamic behaviour of the pocket after ligand binding.


        '''],
        'links':['https://pubmed.ncbi.nlm.nih.gov/35381996/', 'https://chemrxiv.org/engage/chemrxiv/article-details/60c74e33337d6c1fcfe27f43']}


# rpa_metrics = pd.DataFrame([['Overall',66.4, 72.5],['printed rx',54.6, 64.6],['handwritten',67.3,73.3]], columns=['category','ds','non-ds'])
# rapid_metrics = pd.DataFrame([['printed',91.6,70,79.4],['handwritten',21.1,34.7,26.2],['Brute-Force_Printed',29.9,82.7,41.8],['Brute-Force_Handwritten',0.2,62,0.3]],columns=['category','precision','recall','f1_score'])
# rapid_metrics = rapid_metrics.set_index(['category'])

skill_col_size = 5
embed_component= {'linkedin':"""<script src="https://platform.linkedin.com/badges/js/profile.js" async defer type="text/javascript"></script>
        <div class="badge-base LI-profile-badge" data-locale="en_US" data-size="medium" data-theme="light" data-type="VERTICAL" data-vanity="mohamed-fadlalla-ds" data-version="v1"><a class="badge-base__link LI-simple-link" href="https://sd.linkedin.com/in/mohamed-fadlalla-ds?trk=profile-badge"></a></div>""", 'medium':"""<div style="overflow-y: scroll; height:500px;"> <div id="retainable-rss-embed" 
data-rss="https://medium.com/feed/retainable,https://medium.com/feed/data-science-in-your-pocket"
data-maxcols="3" 
data-layout="grid"
data-poststyle="inline" 
data-readmore="Read the rest" 
data-buttonclass="btn btn-primary" 
data-offset="0"></div></div> <script src="https://www.twilik.com/assets/retainable/rss-embed/retainable-rss-embed.js"></script>
              """}

