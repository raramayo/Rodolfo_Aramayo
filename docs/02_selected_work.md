---
title: Selected Research
description: Selected computational biology studies by Rodolfo Aramayo and the Aramayo Lab: biological questions, contributions, public outputs, and current research status.
---

# Selected Research

Our work connects biological questions to computational methods, interpretable results, and reusable research resources. These examples distinguish published findings, released tools, and ongoing investigations.

## MutScan: model audit and evidence integration

<p class="ra-status ra-status--large">Ongoing methodological research · Manuscripts in preparation</p>

**Question.** What do protein language model scores measure, and how much distinct evidence do they contribute to variant interpretation?

**Contribution.** Rodolfo is developing a per-protein model-audit and evidence-integration program across **15 disease-associated human proteins**. It compares zero-shot ESM-family scores with site and substitution-type baselines, structural context, physicochemical features, and curated variant evidence.

**Current output.** A methodological rationale and an analysis program with explicit baselines, checkpoint comparisons, and computational reproducibility checks. Biological findings remain provisional while manuscripts and supporting artifacts are prepared.

### Workstream 1 — What do protein language models actually add? { #large-protein-models-for-variant-prediction }

For each protein, a complete 19 × L mutational scan is decomposed into fitted position effects, amino-acid exchange effects, and an unexplained remainder. The decomposition uses sequence and model outputs without fitting clinical labels.

<figure class="ra-model-map">
  <div class="ra-model-map__input"><strong>Protein sequence + model scores</strong><span>One score for each of 19 substitutions at each position</span></div>
  <div class="ra-model-map__branches">
    <div><strong>Position</strong><span>Effects shared across substitutions at a site</span></div>
    <div><strong>Exchange</strong><span>Effects shared by a directional amino-acid change</span></div>
    <div><strong>Residual</strong><span>What the fitted additive model leaves unexplained</span></div>
  </div>
  <figcaption>Conceptual decomposition, not a results plot. The residual must be tested for repeatability and biological relevance.</figcaption>
</figure>

### Workstream 2 — Evidence integration across 15 proteins

PLMs, substitution matrices, and other predictors can share evolutionary information. This work asks where agreement represents distinct evidence and where it repeats the same signal. The aim is to identify which gene-specific structural, functional, or other evidence should be investigated next.

??? info "Model scope and computational verification"

    The evaluation program includes ESM1b, ESM1v, ESM2 models through 15 billion parameters, ESMC, and ESM3. It uses per-protein ROC/AUROC analysis, stratified benchmarks, parameter-scaling studies, and structural context.

    Five independently seeded ESM1v ensemble checkpoints support checkpoint-to-checkpoint repeatability analysis. Separately, 84 internal replicate workflow runs verified bit-deterministic outputs under the tested configurations, with per-run provenance manifests.

    Checkpoints are not biological replicates, and workflow repeatability is not evidence of clinical validity. This work evaluates existing protein foundation models; it does not claim to train them.

[Read the MutScan methods](03_variant_prediction_rationale.md){ .md-button .md-button--primary }

### LLM-assisted scientific workflows

MutScan also illustrates how Rodolfo uses **Claude and other LLM-based assistants** across software development, comparative analysis, and scientific writing. He directs the biological questions, analytical choices, and interpretation; assistant-generated code and prose are working material to inspect and test.

**Pipeline development.** LLM-assisted development helped turn an RNASE1-specific prototype into a protein-general workflow accepting configurations, FASTA files, or raw sequences. Optional annotations, explicit scoring conventions, and run manifests make inputs, computational settings, and outputs easier to trace.

**Claude-assisted analysis.** Downstream work connects configurable cross-protein comparisons, ensemble-versus-single-model diagnostics, disagreement audits, figure preparation, and manuscript development. This is distinct from the ESM protein language models being evaluated: Claude assists the research process; ESM models supply biological sequence scores.

**Verification in practice.** Development records include configuration checks that caught a parameter-scoping error, repeatability checks under specified settings, and comparisons of figure annotations and manuscript quantities with their source tables. Scientific review also examines whether agreement reflects shared evidence and whether benchmark labels are independent of the predictors being tested.

The emphasis is on making AI-assisted work inspectable and correcting errors—not treating a plausible response or agreement among models as validation. These are research workflows under development; their repositories remain private, and the manuscript is in preparation.

## Computational genomics

### Microbial genome assembly and comparative genomics

<p class="ra-status">Peer-reviewed · 2022 and 2025</p>

**Question.** What do microbial genomes reveal about biological capacity and evolutionary differences?

**Contribution.** Rodolfo co-authored genome assembly, annotation, and comparative-genomics studies of *Myxococcus xanthus* and *Drosophila*-associated *Spiroplasma*.

**Published outputs.** A complete *M. xanthus* DZ2 genome assembly and annotation, and a draft-genome study of three *Spiroplasma* strains that inferred diverse toxin repertoires alongside limited metabolic capacities. These studies provide sequence resources and biological hypotheses for subsequent work.

- **Aramayo R, Nan B.** *De Novo Assembly and Annotation of the Complete Genome Sequence of Myxococcus xanthus DZ2.* *Microbiology Resource Announcements*. 2022;11(5):e0107421. [Paper](https://doi.org/10.1128/mra.01074-21) · [Assembly record](https://doi.org/10.5281/zenodo.6359694).
- **Ramirez P, Martinez Montoya H, Aramayo R, Mateos M.** *Diverse toxin repertoire but limited metabolic capacities inferred from the draft genome assemblies of three Spiroplasma strains associated with Drosophila.* 2025. [Paper](https://doi.org/10.1099/mgen.0.001408).

### Reanalysis of public transcriptomic data

<p class="ra-status">Preprint · 2024</p>

**Question.** What additional biological signal can be recovered from an existing dataset?

**Contribution and output.** Rodolfo co-authored a reanalysis of a *Drosophila melanogaster* dataset that identified an additional set of genes associated with the post-mating response. The preprint and research record document the work.

[Preprint](https://doi.org/10.1101/2024.04.10.588867) · [Research record](https://doi.org/10.5281/zenodo.10928217)

### Sequence duplication and transcriptional profiling

<p class="ra-status">Public research artifact · Related manuscript in preparation</p>

**Question.** How do duplicated sequences and annotation choices affect expression measurements?

**Current work.** Rodolfo investigates the ambiguity introduced when reads from related genomic regions do not support a unique assignment. This connects biological interpretation to the assumptions used in quantification.

[Public research artifact](https://doi.org/10.5281/zenodo.11122398)

## Experimental genetics foundation

<p class="ra-status">Peer-reviewed</p>

Rodolfo's experimental work established a foundation in developmental gene regulation, RNA biology, and sequence recognition during fungal meiosis. It includes the first report of meiotic transvection in fungi and subsequent studies of unpaired DNA and meiotic silencing in *Neurospora crassa*.

That experience informs the laboratory's computational questions: which mechanism could explain a result, which controls are missing, and what experiment could distinguish competing explanations?

[Meiotic transvection — Cell](https://doi.org/10.1016/S0092-8674(00)80081-1) · [Unpaired DNA and silencing — Genetics](https://doi.org/10.1534/genetics.167.1.131) · [Neurospora epigenetics review](https://doi.org/10.1101/cshperspect.a017921)

## Open scientific software

### Manuscript Multi-Target LaTeX Template

<p class="ra-status">Released software · v1.0.0 · August 2026</p>

**Problem.** Maintaining separate manuscript copies for different publication profiles can introduce formatting and content drift.

**Contribution.** One authoritative LaTeX source produces arXiv, bioRxiv, Zenodo, and neutral PDF profiles, with shared content, figures, citations, bibliography, and layout. The repository includes a build driver and dependency checks.

**Public output.** A versioned software release with source code and documentation. The profiles support preparation; submission requirements still need to be checked for the destination.

[Zenodo release](https://zenodo.org/records/22018962){ .md-button .md-button--primary }
[Code & documentation](https://github.com/raramayo/Manuscripts_Templates_Latex){ .md-button }

Other released tools address recurring analysis tasks:

- [HeatMap_Tables_Python](https://doi.org/10.5281/zenodo.15214452) — heat-map table generation and analysis.
- [Taxonomy_Fasta_Headers_Python](https://doi.org/10.5281/zenodo.15216319) — taxonomy-aware FASTA header processing.
- [Fasta_GFF3_Equalizer_Bash](https://doi.org/10.5281/zenodo.12209207) — sequence and annotation reconciliation.

## Research across the laboratory

Brian White's work connects comparative proteomics with protein structure and dynamics. Julen Gamboa studies circadian behavior and comparative genomic architecture. Former undergraduate projects examine isoform evolution, sequencing-data quality, and primate protein conservation.

[People & projects](04_lab.md){ .md-button }
[Publications & software](05_publications.md){ .md-button }
