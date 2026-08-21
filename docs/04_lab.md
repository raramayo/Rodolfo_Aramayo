---
title: Aramayo Lab | People & Projects
description: Meet current and former Aramayo Lab researchers and explore how their projects connect protein variation, comparative genomics, evolutionary biology, and reproducible computation.
---

# Aramayo Lab: People & Projects

<p class="ra-page-lede ra-page-lede--compact">The Aramayo Lab is an interdisciplinary research group in the Department of Biology at Texas A&amp;M University. We integrate computational genomics, bioinformatics, and large language models to investigate molecular and evolutionary biology, with reproducibility as a core requirement throughout the research process.</p>

The laboratory is led by **Rodolfo Aramayo, PhD**, Associate Professor of Biology. Our projects differ in biological system and scale, but share a common method: start with a consequential biological question, make the computational evidence auditable, and distinguish what the data establish from what remains a hypothesis.

<section class="ra-proof" aria-label="Aramayo Lab research themes">
  <div><strong>Proteins</strong><span>Variation, structure, dynamics, allostery, and model evaluation</span></div>
  <div><strong>Genomes</strong><span>Comparative architecture, isoforms, regulation, annotation, and evolution</span></div>
  <div><strong>Evidence</strong><span>Reproducibility, data quality, provenance, and calibrated interpretation</span></div>
</section>

## How the projects fit together

<div class="ra-card-grid ra-card-grid--three ra-lab-themes">
  <article class="ra-card">
    <p class="ra-card__number">PROTEIN VARIATION</p>
    <h3>From sequence scores to mechanism</h3>
    <p>MutScan evaluates protein-language-model scores. Brian White's work extends the question toward proteome-scale comparison, predicted and experimental structures, molecular dynamics, and residue-communication networks.</p>
  </article>
  <article class="ra-card">
    <p class="ra-card__number">COMPARATIVE GENOMICS</p>
    <h3>From conserved sequence to phenotype</h3>
    <p>Julen Gamboa, Daniel Nguyen, and Mariana Fauteux examine variation at complementary scales: regulatory loci and behavior, alternatively spliced isoforms, and highly conserved proteins across primates.</p>
  </article>
  <article class="ra-card">
    <p class="ra-card__number">RESEARCH PRACTICE</p>
    <h3>Make the evidence inspectable</h3>
    <p>Joseph Gallucci's audit of public sequencing data makes a laboratory-wide principle explicit: metadata, coverage, annotation quality, provenance, and limitations are part of a result—not administrative details.</p>
  </article>
</div>

## Current graduate students

<div class="ra-people-grid ra-people-grid--current">
  <article class="ra-person-card">
    <header class="ra-person-card__header">
      <div>
        <p class="ra-status">Current graduate student</p>
        <h3>Brian White</h3>
      </div>
      <span class="ra-topic-tag">Protein systems</span>
    </header>
    <p>Brian develops computational approaches that connect proteome-scale comparison with protein structure and dynamics.</p>
    <div class="ra-project-list">
      <div><strong>Composition-based comparative proteomics</strong><span>His graduate research tests amino-acid composition profiles as a tractable screening layer for candidate reciprocal substitutions and phenotype-associated differences across large proteome collections. Preliminary pipeline results guide broader analyses that remain in progress.</span></div>
      <div><strong>Proteins as dynamic networks</strong><span>A manuscript in preparation integrates structure prediction, molecular dynamics, allostery, and graph analysis into a reproducible framework for interpreting proteins as communicating ensembles rather than static objects.</span></div>
      <div><strong>Mutation responses in human RNase 1</strong><span>An ongoing study compares AlphaFold3-derived and experimentally determined starting structures to ask whether similar static models yield different dynamic or residue-network responses to mutation. No study results are claimed here.</span></div>
    </div>
    <p class="ra-connection"><strong>Connection to the lab.</strong> Brian's work carries the laboratory's model-auditing philosophy from sequence-level scores toward structure-aware and dynamics-aware interpretation of protein variation.</p>
  </article>

  <article class="ra-person-card">
    <header class="ra-person-card__header">
      <div>
        <p class="ra-status">Current graduate student</p>
        <h3>Julen Gamboa</h3>
      </div>
      <span class="ra-topic-tag">Circadian genomics</span>
    </header>
    <p>Julen investigates how natural genomic variation among inbred mouse strains relates to circadian behavior, connecting organism-level measurements to gene structure and regulatory architecture.</p>
    <div class="ra-project-list">
      <div><strong>Completed behavioral synthesis</strong><span>He reconciled 260 circadian-relevant measurements from seven public studies into evidence-based day-night behavioral profiles for 16 strains. An initial clustering analysis produced no stable groupings, so the project shifted to more interpretable within-strain effect estimates.</span></div>
      <div><strong>Comparative locus analysis</strong><span>Ongoing work examines sequence conservation, locus architecture, and annotation quality across 28 circadian genes. Preliminary alignments nominate candidate structural and annotation differences for formal review.</span></div>
      <div><strong>Regulatory integration</strong><span>Proposed analyses will combine phylogenetics, pangenome graphs, motif mapping, and DNA language models to test—not assume—whether coding, structural, and cis-regulatory variation helps explain behavioral differences.</span></div>
    </div>
    <p class="ra-connection"><strong>Connection to the lab.</strong> Julen's work extends comparative genomics toward a multiscale genotype-to-phenotype question while keeping annotation quality, negative results, controls, and evidentiary limits visible.</p>
  </article>
</div>

## Former undergraduate researchers

<p class="ra-section-intro">These projects show how undergraduate researchers contributed substantive analyses to the laboratory's broader scientific program. The descriptions report project-specific results and do not generalize beyond the datasets analyzed.</p>

<div class="ra-people-grid ra-people-grid--former">
  <article class="ra-person-card">
    <header class="ra-person-card__header">
      <div>
        <p class="ra-status">Former undergraduate student · 2025 thesis</p>
        <h3>Daniel Nguyen</h3>
      </div>
      <span class="ra-topic-tag">Isoform evolution</span>
    </header>
    <h4>Predicting iso-orthology for human CARS1 isoforms</h4>
    <p>Daniel developed an isoform-level comparative framework for human cysteinyl-tRNA synthetase 1 (CARS1) and four nonhuman hominid species. He combined enhanced reciprocal-best-hit analysis with tissue-expression data, sequence alignment, coding-sequence comparison, and protein-domain annotation.</p>
    <p>His Undergraduate Research Scholars thesis identified conserved isoform-specific features and showed how incomplete annotations can complicate isoform-orthology calls. The work moves comparative analysis beyond gene-level labels toward reproducible study of transcript and protein diversity; proposed functional interpretations still require experimental validation.</p>
  </article>

  <article class="ra-person-card">
    <header class="ra-person-card__header">
      <div>
        <p class="ra-status">Former undergraduate student · Research poster</p>
        <h3>Joseph Gallucci</h3>
      </div>
      <span class="ra-topic-tag">Data quality</span>
    </header>
    <h4>Auditing public next-generation sequencing submissions</h4>
    <p>Joseph audited 25 randomly selected, cancer-related human whole-genome datasets from the NCBI Sequence Read Archive, extracting metadata and estimating coverage across their sample runs.</p>
    <p>Within that selected set, 11 datasets exceeded 1× average coverage and six exceeded 4×. The variability raised practical questions about whether deposited metadata and coverage support reproducible reanalysis. His project reinforces a central lab principle: the quality and provenance of public data must be evaluated before downstream biological conclusions are trusted.</p>
  </article>

  <article class="ra-person-card">
    <header class="ra-person-card__header">
      <div>
        <p class="ra-status">Former undergraduate student · Research poster</p>
        <h3>Mariana Fauteux</h3>
      </div>
      <span class="ra-topic-tag">Primate proteomics</span>
    </header>
    <h4>Highly conserved proteins across primate species</h4>
    <p>Mariana screened proteomes from 26 primate species using stringent 100% sequence-identity and full-length-coverage clustering, proteome-completeness assessment, and protein-domain annotation.</p>
    <p>Her analysis reported 50 highly conserved protein clusters in the selected proteomes and highlighted histones, ribosomal proteins, and other strongly constrained functions. The project demonstrates how careful curation and explicit thresholds can turn large comparative datasets into testable hypotheses about evolutionary constraint.</p>
  </article>
</div>

## Mentoring and research culture

My mentoring emphasizes biological reasoning, intellectual independence, reproducible workflows, clear documentation, and honest interpretation of uncertainty. Students learn to move from public data and computational tools to a defensible scientific argument—and to recognize when annotation quality, study design, or model assumptions limit that argument.

Project descriptions on this page were prepared from research materials supplied for this site revision. Private proposals, theses, manuscripts, and poster files remain outside the public website repository. Active work is labeled as ongoing or proposed; it should not be read as a peer-reviewed finding or a clinical claim.

<div class="ra-actions">
  <a class="md-button md-button--primary" href="../02_selected_work/">Explore the laboratory's selected research</a>
  <a class="md-button" href="../04_teaching/">Read about teaching and mentorship</a>
  <a class="md-button" href="https://zenodo.org/communities/aramayo_lab/records?q=&amp;l=list&amp;p=1&amp;s=10&amp;sort=newest">Browse public Aramayo Lab outputs</a>
</div>
