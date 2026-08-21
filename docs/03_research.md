---
title: Research Focus
description: Research in protein model auditing, variant interpretation, computational genomics, and molecular genetics.
---

# Research Focus

My research asks how biological sequence encodes function—and how computational systems can interpret that information without losing biological context, quantitative rigor, or reproducibility.

## Protein model auditing for variant interpretation

My current priority is determining what zero-shot ESM-family protein language model scores measure, when their signal is valid, and how that signal should be combined with gene-specific biological evidence.

This work includes:

- zero-shot variant scoring with ESM1b, ESM1v, ESM2, ESMC, and ESM3;
- per-protein decomposition of scores into site-level, substitution-type, and residual score components;
- comparison with explicit additive main-effects models and classical substitution matrices;
- per-protein ROC/AUROC and stratified benchmark analysis;
- model parameter-scaling and accuracy-versus-compute studies;
- integration with ClinVar, dbSNP, Ensembl, HGVS, and MANE Select;
- use of AlphaFold pLDDT confidence and structural context;
- analysis of benchmark circularity and dependence among evidence sources;
- checkpoint repeatability, workflow reproducibility, and explicit failure analysis; and
- gene-specific interpretation of model behavior using evolutionary and structural biology.

The principal current project, MutScan, is a model-evaluation and evidence-integration research program spanning 15 disease-associated human proteins. It examines unique and shared signal rather than assuming that agreement among methods represents independent confirmation.

**Status:** Research in progress; manuscript in preparation (2026).

[Read why this analysis matters](03_variant_prediction_rationale.md){ .md-button .md-button--primary }
[View the selected-work overview](02_selected_work.md#large-protein-models-for-variant-prediction){ .md-button }

## Computational genomics and bioinformatics

### Genome assembly and comparative genomics

I have contributed to complete and draft microbial genome assemblies, including *Myxococcus xanthus* and multiple *Spiroplasma* strains. My interests include comparative genome architecture, sequence variation, annotation quality, and reproducible genome-analysis workflows.

### Transcriptomics and multiomics

My experience spans genomic, epigenomic, and transcriptomic analysis using Illumina, PacBio, and Ion Torrent data. It includes bulk and single-cell assays, differential expression, pathway enrichment, motif discovery, and regulatory-network inference.

A current project examines how sequence duplication and genome annotation affect transcriptional-profiling measurements in the human genome.

### Open scientific software and scalable computing

I develop scientific workflows in Python, R, and Bash/Shell and deploy analyses across local, HPC, and cloud environments. My work emphasizes version control, provenance, deterministic execution, portability, and transparent reporting.

Our latest contribution to reproducible manuscript preparation is the [Manuscript Multi-Target LaTeX Template v1.0.0](https://zenodo.org/records/22018962). It keeps one authoritative manuscript source while producing arXiv, bioRxiv, Zenodo, and neutral PDF profiles; the [source code and documentation are available on GitHub](https://github.com/raramayo/Manuscripts_Templates_Latex).

## Experimental foundation

My computational research is grounded in molecular genetics, genome engineering, epigenetics, and RNA biology. Earlier work investigated developmental gene regulation in *Aspergillus nidulans* and sequence recognition and RNA-mediated meiotic silencing in *Neurospora crassa*.

This biological foundation informs how I evaluate computational and AI systems: predictions must be assessed not only statistically, but also in the context of mechanism, experimental design, evolutionary history, evidence dependence, and the limitations of the underlying data.

[Meet the Aramayo Lab](04_lab.md) · [View selected work](02_selected_work.md) · [View publications and software](05_publications.md)
