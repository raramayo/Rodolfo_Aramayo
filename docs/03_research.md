---
title: Research Approach
description: How the Aramayo Lab connects experimental biology, comparative genomics, biological model evaluation, and reproducible scientific workflows.
---

# Research Approach

We study how biological sequences encode function and how computational evidence can help explain variation. Our work connects experimental molecular genetics with genome-scale analysis and the evaluation of biological AI.

## Start with the biological question

A useful analysis begins with the organism, phenotype, and experimental context. Sequence quality, annotation choices, appropriate controls, and the limits of a measurement shape what can be concluded. We use those constraints to decide which comparisons are informative and which hypotheses need additional data.

This approach connects projects across protein variation, microbial genomics, transcriptional profiling, and comparative analysis. [Explore selected research](02_selected_work.md).

## Protein model auditing for variant interpretation

MutScan asks what zero-shot ESM-family protein language model scores measure and how their signals relate to gene-specific biological evidence. The program spans **15 disease-associated human proteins** and connects two questions:

- How much of a model's score can be explained by position and substitution-type effects, and what remains?
- When model scores, physicochemical features, structural context, and curated variant evidence agree, how much information is genuinely distinct?

The work includes explicit baselines, checkpoint comparisons, per-protein benchmarks, and failure analysis. Current findings are provisional; manuscripts are in preparation. Model scores are research evidence and do not establish a clinical classification.

[MutScan methods](03_variant_prediction_rationale.md){ .md-button .md-button--primary }

## Computational genomics and bioinformatics

Our published work includes microbial genome assembly, annotation, comparative genomics, and transcriptomic reanalysis. Current research also examines how sequence duplication and annotation affect transcriptional-profiling measurements.

These projects share a practical concern: biological interpretation depends on how reads, transcripts, genes, and proteins are represented and compared. A computational result becomes more useful when the assumptions behind those representations are visible.

Graduate and former undergraduate projects extend this work into circadian loci, isoform evolution, proteome conservation, and the quality of public sequencing data.

[Genomics studies](02_selected_work.md#computational-genomics){ .md-button }
[People & projects](04_lab.md){ .md-button }

## Open scientific software and scalable computing

Rodolfo develops scientific workflows in Python, R, and Bash/Shell, with experience across Linux, HPC, and cloud environments. Version control, provenance, repeatable execution, and clear reporting support both research and teaching.

Claude and other LLM assistants contribute to software development, analytical exploration, and scientific writing within this process. In [MutScan's LLM-assisted workflow](02_selected_work.md#llm-assisted-scientific-workflows), biological judgment, baseline comparisons, and checks against source data guide how those contributions are used.

The [Manuscript Multi-Target LaTeX Template v1.0.0](https://zenodo.org/records/22018962) extends this reproducibility focus to manuscript preparation. One authoritative source produces arXiv, bioRxiv, Zenodo, and neutral PDF profiles; [code and documentation are available on GitHub](https://github.com/raramayo/Manuscripts_Templates_Latex).

## Experimental foundation

Rodolfo's experimental research in fungal genetics, gene regulation, RNA biology, and meiotic silencing informs how the lab interprets computational results. Mechanism, evolutionary history, and experimental design provide context for deciding which conclusions are supported and what should be tested next.

[Experimental genetics](02_selected_work.md#experimental-genetics-foundation){ .md-button }
[Research capabilities](02_Professional_Skills.md){ .md-button }
