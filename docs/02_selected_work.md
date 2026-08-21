---
title: Selected Work
description: Selected work in protein model auditing, missense-variant evidence integration, computational genomics, and experimental genetics.
---

# Selected Work

My work connects biological mechanism, quantitative model evaluation, and reproducible scientific software. Current research is labeled separately from peer-reviewed and publicly released work.

## MutScan: model audit and evidence integration

<p class="ra-status ra-status--large">Active methodological research · Manuscripts in preparation (2026)</p>

MutScan is a reproducibility-aware research program for evaluating missense-variant signals across 15 disease-associated human proteins. It connects two workstreams: auditing what protein language model (PLM) scores contain and examining how multiple evidence sources overlap or contribute distinct information.

### Workstream 1 — What do protein language models actually add? { #large-protein-models-for-variant-prediction }

My current priority is determining what zero-shot PLM scores contain—not only how well they rank a benchmark. A strong performance number does not, by itself, establish which biological signal is reflected in a score or whether that signal supports the interpretation being attempted.

For each protein, I am analyzing a complete 19 × L mutational scan and asking how much of the PLM score can be described by an additive main-effects model—site plus substitution-type effects, without their interaction—and how much remains unexplained.

<div class="ra-card-grid ra-card-grid--three ra-signal-grid">
  <article class="ra-card">
    <p class="ra-card__number">SITE</p>
    <h3>Position-level component</h3>
    <p>Captures systematic differences among positions, including constraint-related signal.</p>
  </article>
  <article class="ra-card">
    <p class="ra-card__number">SUBSTITUTION</p>
    <h3>Amino-acid exchange component</h3>
    <p>Captures substitution-type effects that can be compared with classical matrices such as BLOSUM62.</p>
  </article>
  <article class="ra-card">
    <p class="ra-card__number">RESIDUAL</p>
    <h3>Residual component</h3>
    <p>Measures what the additive main-effects model does not explain and tests whether that remainder is reproducible.</p>
  </article>
</div>

The decomposition is computed from model outputs and sequence alone, without clinical labels. This creates a label-independent way to measure the fitted additive main effects, compare the substitution-type component with a classical matrix such as BLOSUM62, and quantify the residual before asking whether any of those signals are clinically informative.

[Read the full research rationale](03_variant_prediction_rationale.md){ .md-button .md-button--primary }

#### Model-evaluation program

The wider program evaluates ESM1b, ESM1v, ESM2 models through 15 billion parameters, ESMC, and ESM3 for zero-shot variant scoring. It combines per-protein ROC/AUROC analysis, stratified benchmarks, parameter-scaling studies, AlphaFold pLDDT and structural context, curated variant evidence, and explicit failure-mode analysis.

Five independently seeded ESM1v ensemble checkpoints support checkpoint-to-checkpoint repeatability analysis. They are kept conceptually separate from the 84-run workflow verification used to test computational reproducibility.

This work evaluates systems built on existing protein foundation models; it does not claim to train those foundation models.

### Workstream 2 — Evidence integration across 15 proteins

The multi-evidence workstream examines how model scores, rule-based physicochemical features, curated clinical evidence, and structural context overlap or contribute distinct information.

The framework does not assume that agreement among methods represents independent confirmation. PLMs, substitution matrices, and other predictors can share evolutionary information, so the analysis examines evidence dependence rather than counting every agreeing score as a separate vote.

Across my current model-evaluation work, reproducibility is treated as part of correctness. Internal workflow verification produced bit-deterministic outputs across 84 replicate runs under the tested configurations, with per-run provenance manifests connecting inputs, outputs, and execution environments. Separately, the system is designed for portable CPU and GPU execution and for regression testing as methods evolve.

The objective is not simply another score. The work is designed to clarify where current methods apply, where they do not, and which categories of gene-specific structural, functional, population, or clinical evidence should be investigated next. Because this research is ongoing, its findings are provisional until manuscripts and supporting artifacts are publicly released.

### Related current work

- **Proteins as Dynamic Networks: Linking Sequence, Structure, Allostery, and Molecular Motion** — Brian White and Rodolfo Aramayo; review manuscript in preparation; [public research record](https://zenodo.org/records/18999780).
- **Comparing Mutation Responses in Predicted and Experimentally Determined Human RNase 1 Structures** — Brian White and Rodolfo Aramayo; ongoing structure-and-dynamics analysis. The supplied project introduction reports the research questions and methods, not study results.
- **Composition-Based Comparative Proteomics** — Brian White; graduate research using amino-acid profiles to screen proteome collections for candidate reciprocal substitutions and phenotype-associated differences. Broader comparative analyses remain in progress.

[Meet the researchers and see how these projects connect](04_lab.md){ .md-button }

## Computational genomics

### Sequence duplication and transcriptional profiling

<p class="ra-status">Public research artifact (2024) · Related manuscript in preparation</p>

I study how duplicated sequences and genome-annotation choices can affect transcriptional-profiling measurements in the human genome. This work examines a fundamental source of ambiguity: reads originating from related genomic regions may not support a single, unambiguous assignment.

[View the public research artifact](https://doi.org/10.5281/zenodo.11122398){ .md-button }

### Microbial genome assembly and comparative genomics

<p class="ra-status">Peer-reviewed</p>

My computational-genomics work includes complete and draft genome assembly, annotation, and comparative analysis across bacterial systems.

- **Diverse toxin repertoire but limited metabolic capacities inferred from the draft genome assemblies of three *Spiroplasma* strains associated with *Drosophila*.** *Microbial Genomics*, 2025. [Read the publication](https://doi.org/10.1099/mgen.0.001408).
- **De Novo Assembly and Annotation of the Complete Genome Sequence of *Myxococcus xanthus* DZ2.** *Microbiology Resource Announcements*, 2022. [Read the publication](https://doi.org/10.1128/mra.01074-21) · [View the assembly record](https://doi.org/10.5281/zenodo.6359694).

### Reanalysis of public transcriptomic data

<p class="ra-status">Preprint (2024)</p>

I co-authored a reanalysis of an existing *Drosophila melanogaster* dataset that identified an additional set of genes associated with the post-mating response.

[Read the preprint](https://doi.org/10.1101/2024.04.10.588867) · [View the research record](https://doi.org/10.5281/zenodo.10928217)

## Experimental genetics foundation

<p class="ra-status">Peer-reviewed</p>

My computational work is grounded in experimental molecular genetics. Earlier research includes the first report of meiotic transvection in fungi and subsequent studies of sequence recognition, Argonaute-associated meiotic silencing, and the properties of unpaired DNA in *Neurospora crassa*.

- [Meiotic transvection in fungi — *Cell*, 1996](https://doi.org/10.1016/S0092-8674(00)80081-1)
- [Properties of unpaired DNA required for efficient silencing — *Genetics*, 2004](https://doi.org/10.1534/genetics.167.1.131)
- [*Neurospora crassa* as a model for epigenetics — *Cold Spring Harbor Perspectives in Biology*, 2013](https://doi.org/10.1101/cshperspect.a017921)

## Open scientific software

Selected public releases include:

- [Manuscript Multi-Target LaTeX Template v1.0.0](https://zenodo.org/records/22018962) — our latest open-software release for reproducible manuscript preparation. It uses one authoritative manuscript source to produce arXiv, bioRxiv, Zenodo, and neutral PDF profiles while keeping content, figures, citations, bibliography, and layout shared; [source code and documentation on GitHub](https://github.com/raramayo/Manuscripts_Templates_Latex).
- [HeatMap_Tables_Python](https://doi.org/10.5281/zenodo.15214452) — reproducible heat-map table generation and analysis.
- [Taxonomy_Fasta_Headers_Python](https://doi.org/10.5281/zenodo.15216319) — taxonomy-aware FASTA header processing.
- [Fasta_GFF3_Equalizer_Bash](https://doi.org/10.5281/zenodo.12209207) — sequence and annotation reconciliation.

[Browse GitHub](https://github.com/raramayo){ .md-button .md-button--primary }
[Browse the Zenodo collection](https://zenodo.org/communities/aramayo_lab/records?q=&l=list&p=1&s=10&sort=newest){ .md-button }
