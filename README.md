# **PersonaGenerator**

A modular, highly configurable Python framework for generating high-fidelity synthetic character profiles. Designed specifically to supply local, uncensored LLM character engines with deep psychological consistency, visceral physical grounding, and rich behavioral friction.

## **⚠️ Content Advisory & Intended Scope**

This repository contains an identity generation framework designed for local LLM character grounding, adult roleplay environments, and behavioral simulation testing.  
Generated profiles include complex psychological neuroses, detailed anatomical/somatic markers, explicit sexual orientation preferences, and adult lifestyle parameters. All profiles are purely synthetic, algorithmically weighted, and text-based. For details, see [SENSITIVE\_CONTENT.md](https://www.google.com/search?q=./SENSITIVE_CONTENT.md).

## **Key Architectural Features**

* **Cascading Core Anchors**: Generates identities bound by core psychological drivers (Enneagram, Temperament, Age, Biological Sex) rather than flat, random assignments.  
* **Psychodynamic Layering**: Tracks somatic armoring, stress disintegration vectors, and integration pathways.  
* **Zero-Rework Modular Architecture**: Standalone attribute modules return uniform key-value strings (Dict\[str, str\]) for seamless extensibility and native loop parsing in output renderers.  
* **Local LLM Grounding**: Outputs structured Markdown files designed to immediately anchor system prompts in complex persona traits, physical micro-expressions, and behavioral flaws.

## **System Architecture & Data Flow**

graph TD  
    A\[Identity Blueprint\] \--\>|Gender, Sex, Age, Orientation| B\[Physical Traits Engine\]  
    A \--\>|Sex, Age, Career, Social Life| C\[Personality Core Anchor Dict\]  
      
    subgraph Upstream Core Anchors  
        C \--\>|Enneagram Type| D\[enneagram\_psychodynamics.py\]  
        C \--\>|Temperament| D  
        C \--\>|Age & Biological Sex| D  
    end  
      
    subgraph Downstream Dependent Modules  
        C \--\> E\[quirks.py\]  
        C \--\> F\[fears\_and\_insecurities.py\]  
        C \--\> G\[sexual\_preferences.py\]  
        C \--\> H\[health\_profiles.py\]  
        C \--\> I\[moral\_compass.py\]  
        I \--\> J\[caregiver\_profiles.py\]  
        C \--\> K\[coachable\_topics.py\]  
        C \--\> L\[skills\_and\_talents.py\]  
    end

    D \--\> M\[Persona Dataclass Engine\]  
    B \--\> M  
    E \--\> M  
    F \--\> M  
    G \--\> M  
    H \--\> M  
    J \--\> M  
    K \--\> M  
    L \--\> M  
      
    M \--\> N\[markdown\_generator.py\]  
    N \--\> O\[.md Persona Profile File\]

## **Data Cascading Pipeline Matrix**

| Execution Order | Engine / Module Layer | Upstream Input Dependencies | Output Attributes & Tokens | Return Data Type |
| :---- | :---- | :---- | :---- | :---- |
| **1\. Identity Blueprint** | PersonaGenerator.py | *Random Uniform Seed* | gender, sex, age, orientation | Primitive Strings |
| **2\. Environment & Lifestyle** | careers\_and\_finance.py culture\_and\_geography.py social\_and\_lifestyle.py | *None* | occupation, financial\_situation, education, region, cultural\_bg | Dict\[str, str\] & Strings |
| **3\. Physical Traits Engine** | physical\_traits.py | gender, sex, age, fashion\_sense | Height, body type, facial markers, anatomical features | Dict\[str, str\] |
| **4\. Core Personality Anchor** | PersonaGenerator.py | enneagram\_type, temperament | favorite\_color, siblings, sense\_of\_humor, social\_behavior | Upstream personality Dict\[str, str\] |
| **5\. Psychodynamics Engine** | enneagram\_psychodynamics.py | enneagram\_type, temperament, age, sex | Instinctual Subtype, Stress Disintegration, Integration Pathway, Somatic Armoring | Dict\[str, str\] |
| **6\. Behavioral & Perception** | quirks.py fears\_and\_insecurities.py | personality, fashion\_sense, physical | quirk, body\_image\_perception | Strings inserted into personality |
| **7\. Preferences Engine** | sexual\_preferences.py | orientation, personality\['enneagram\_type'\] | Kinks, dynamic thresholds, intimacy preferences | Dict\[str, str\] |
| **8\. Health & Morality Engine** | health\_profiles.py moral\_compass.py caregiver\_profiles.py | age, career, personality, physical | health, moral\_compass, caregiver\_style | Dict\[str, str\] & Strings |
| **9\. Document Renderer** | markdown\_generator.py | Complete Persona Dataclass Instance | Formatted Markdown File saved to ./md/ | File I/O (.md) |

## **Repository Directory Structure**

Plaintext  
PersonaGenerator/  
├── md/                            \# Generated persona output directory  
├── PersonaGenerator.py            \# Main orchestrator script & entry point  
├── enneagram\_psychodynamics.py    \# Psychodynamic, somatic armoring & subtype engine  
├── caregiver\_profiles.py          \# Contextual caregiving and relational style asset  
├── careers\_and\_finance.py         \# Career, income tier, and education background asset  
├── coachable\_topics.py            \# Personal growth and development areas module  
├── culture\_and\_geography.py       \# Regional and cultural background asset  
├── fears\_and\_insecurities.py      \# Fears and bodily perception narrative engine  
├── health\_profiles.py             \# Contextual physical and mental health profiles  
├── hobbies.py                     \# Weighted hobbies and leisure activities  
├── markdown\_generator.py          \# Persona dataclass to Markdown exporter  
├── moral\_compass.py               \# Ethical frameworks and moral drivers asset  
├── names.py                       \# Gender-aligned given name generator  
├── physical\_traits.py             \# Anatomical and physical marker generator  
├── quirks.py                      \# Behavioral quirks and contextual habits module  
├── sexual\_preferences.py          \# Weighted kink and orientation preference matrix  
├── skills\_and\_talents.py          \# Weighted skill sets based on career/personality  
├── social\_and\_lifestyle.py        \# Social style, fashion, and tech usage asset  
├── surnames.py                    \# Surname database generator  
├── SENSITIVE\_CONTENT.md           \# Content scope and usage advisory  
└── README.md                      \# Architecture documentation

## **Quick Start**

### **Prerequisites**

* Python 3.9 or higher

### **Installation & Execution**

Bash  
\# Clone the repository  
git clone https://github.com/Mimi-B125/PersonaGenerator.git  
cd PersonaGenerator

\# Run the generator suite  
python PersonaGenerator.py

Follow the terminal prompt to specify the number of personas to batch-generate. Output markdown files will be automatically rendered inside the ./md/ directory.  
