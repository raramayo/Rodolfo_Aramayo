---
title: What Protein Language Models Actually Add
description: The MutScan rationale for decomposing protein-language-model scores, testing their residual signal, and defining where they can support variant interpretation.
---

# What do protein language models actually add?

<p class="ra-status ra-status--large">Active methodological research · Manuscript in preparation (2026)</p>

<p class="ra-page-lede">Better variant prediction requires understanding what a model measures—not only how well it ranks a benchmark.</p>

Within MutScan, I am developing a per-protein analysis of zero-shot ESM scores. The objective is to determine how much of each score reflects site-level effects and general amino-acid substitution patterns, how much remains unexplained by an additive main-effects model, and whether that residual is reproducible across independently trained model checkpoints.

This is the question that connects my background in molecular genetics, evolutionary biology, computational genomics, statistical design, and scientific software: **when is an AI result biologically meaningful, where might it fail, and what evidence should come next?**

<section class="ra-proof" aria-label="Current methodological scope">
  <div><strong>19 × L</strong><span>Single amino-acid substitutions examined for each protein</span></div>
  <div><strong>5</strong><span>Independently seeded ESM1v checkpoints used for sensitivity analysis</span></div>
  <div><strong>84</strong><span>Internal replicate workflow runs used to verify deterministic execution under tested configurations</span></div>
</section>

## The distinction that matters

<div class="ra-card-grid ra-card-grid--two">
  <article class="ra-card">
    <p class="ra-card__number">EVOLUTIONARY EFFECT</p>
    <h3>Deleteriousness</h3>
    <p>Refers to reduced organismal fitness. Many computational tools instead estimate related evolutionary-constraint or molecular-effect signals that can be used as evidence about a variant.</p>
  </article>
  <article class="ra-card">
    <p class="ra-card__number">CLINICAL INTERPRETATION</p>
    <h3>Pathogenicity</h3>
    <p>Depends on the gene, disease mechanism, inheritance, genotype, penetrance, phenotype, and the total evidence available for a particular variant.</p>
  </article>
</div>

The two concepts are related, but they are not interchangeable. A protein model may identify an evolutionarily unusual substitution without establishing that the allele causes disease in a particular clinical context. MutScan therefore treats model output as evidence to investigate, not as a clinical classification.

## A label-independent decomposition

For a protein of length **L**, **i** identifies one sequence position, **wtᵢ** is the wild-type amino acid at that position, and **b** is one of the other 19 standard amino acids. The log-likelihood-ratio score **LLR(i, b)** is the zero-shot model score for substituting wtᵢ with b at position i; it contrasts the model's support for those residues under the selected scoring rule. The complete scan therefore contains 19 × L deterministic model outputs—not 19 × L clinical labels or experimental measurements.

The additive model is fitted separately to each model checkpoint:

<figure class="ra-decomposition">
  <div class="ra-equation" role="math" aria-label="The observed log-likelihood-ratio score at position i for alternative amino acid b equals fitted intercept mu, plus fitted site effect alpha at i, plus fitted substitution effect beta for the wild-type residue at i changing to b, plus residual r at i and b.">
    <span class="ra-equation__formula" aria-hidden="true">
      <span>LLR(i, b) = μ̂</span>
      <span>+ α̂<sub>i</sub></span>
      <span>+ β̂(wt<sub>i</sub> → b)</span>
      <span>+ r(i, b)</span>
    </span>
  </div>

  <dl class="ra-decomposition__terms">
    <div class="ra-decomposition__term">
      <dt><span class="ra-decomposition__symbol">μ̂</span><span>Overall level</span></dt>
      <dd><strong>Fitted intercept.</strong> The shared baseline for the protein's score surface under the chosen coding convention.</dd>
    </div>
    <div class="ra-decomposition__term">
      <dt><span class="ra-decomposition__symbol">α̂ᵢ</span><span>Site</span></dt>
      <dd><strong>Fitted position effect.</strong> The systematic score shift associated with site i across its 19 possible substitutions.</dd>
    </div>
    <div class="ra-decomposition__term">
      <dt><span class="ra-decomposition__symbol">β̂</span><span>Exchange</span></dt>
      <dd><strong>Fitted substitution effect.</strong> The directional wtᵢ → b effect shared across positions with the same wild-type residue. It can be compared with, but is not identical to, BLOSUM62.</dd>
    </div>
    <div class="ra-decomposition__term">
      <dt><span class="ra-decomposition__symbol">r</span><span>Residual</span></dt>
      <dd><strong>Unexplained remainder.</strong> The observed score minus μ̂ + α̂ᵢ + β̂ for this substitution; it is not automatically new biological context.</dd>
    </div>
  </dl>

  <figcaption>A hat marks a fitted term. The additive prediction is μ̂ + α̂ᵢ + β̂(wtᵢ → b); the residual r(i, b) is what that baseline does not explain.</figcaption>
</figure>

Because each site has only one wild-type residue, the design is nested within wild-type-residue classes rather than fully crossed. Explicit coding constraints are therefore required to make the fitted coefficients interpretable. Fitted residuals from separately analyzed checkpoints can then be compared to test checkpoint-level repeatability.

Here, **label-independent** means that the decomposition uses the protein sequence and model outputs without fitting to pathogenic/benign labels. It does not mean that a residual is automatically biologically informative or clinically valid. The analysis first asks three operational questions for each protein:

1. How well can a fitted additive main-effects model—site plus substitution-type effects, without their interaction—describe the PLM scores under the chosen metric?
2. How does the fitted substitution-type component compare with a classical matrix such as BLOSUM62 when placed on a compatible scale?
3. How much residual variation remains, and how repeatable is it across model checkpoints?

A nonzero residual does not automatically establish useful new biology. It becomes interesting only if it is reproducible and can be related to independent structural, functional, evolutionary, population, or clinical evidence.

## Why the analysis is difficult

<div class="ra-card-grid ra-card-grid--two ra-challenge-grid">
  <article class="ra-card">
    <h3>Statistical identifiability</h3>
    <p>Each protein position has only one wild-type residue. Position and substitution effects are therefore nested within wild-type classes, and naive parameterizations can produce rank deficiency or coding-dependent variance attribution.</p>
  </article>
  <article class="ra-card">
    <h3>Checkpoint repeatability</h3>
    <p>One score per substitution does not provide experimental replication. Five independently seeded ESM1v ensemble checkpoints provide a sensitivity analysis for model-to-model variation—not biological replication.</p>
  </article>
  <article class="ra-card">
    <h3>Benchmark circularity</h3>
    <p>Clinical-label benchmarks can be partly circular when variant assertions incorporate computational evidence correlated with the methods being evaluated. A random train/test split does not remove that dependency.</p>
  </article>
  <article class="ra-card">
    <h3>Correlated predictors</h3>
    <p>Substitution matrices, PLMs, and other variant tools can share evolutionary signal. Agreement may therefore repeat one source of evidence rather than provide independent confirmation.</p>
  </article>
  <article class="ra-card">
    <h3>Gene-specific validity</h3>
    <p>Performance differences among proteins may reflect biology, sample size, label quality, class balance, or ascertainment. Per-protein analysis keeps that heterogeneity visible instead of hiding it inside a pooled average.</p>
  </article>
  <article class="ra-card">
    <h3>Biological interpretation</h3>
    <p>Alignment depth, paralog composition, selection regime, structural architecture, and population constraint provide hypotheses for why model behavior differs. These explanations must be tested rather than assumed.</p>
  </article>
</div>

## What the work is designed to deliver

The intended output is not simply another pathogenicity score. It is a protein-by-protein account of:

- the signal recoverable by an explicit additive main-effects model;
- the repeatable residual component of the PLM score;
- the degree to which different evidence sources overlap;
- the conditions under which model scores support a research interpretation; and
- the categories of additional evidence to investigate when a model cannot resolve the question.

This framing turns interdisciplinarity into an operational advantage. The PLM supplies a measurement. Statistical model auditing tests what that measurement contains. Evolutionary, structural, and molecular biology supply candidate explanations. Reproducible software makes the analysis inspectable and repeatable.

## Current status and methodological context

This is ongoing methodological research. The decomposition, cross-protein comparisons, and biological explanations are being evaluated; findings remain provisional until the manuscripts and supporting artifacts are publicly released.

The five ESM1v models used for checkpoint-level sensitivity analysis are independently seeded members of the published ensemble ([paper](https://papers.nips.cc/paper/2021/file/f51338d736f95dd42427296047067694-Paper.pdf) and [supplement](https://papers.nips.cc/paper/2021/file/f51338d736f95dd42427296047067694-Supplemental.pdf)). The separation between computational prediction and clinical classification is consistent with [ACMG/AMP variant-interpretation standards](https://pmc.ncbi.nlm.nih.gov/articles/PMC4544753/) and subsequent [ClinGen recommendations for calibrated PP3/BP4 computational evidence](https://pmc.ncbi.nlm.nih.gov/articles/PMC9748256/).

!!! warning "Research use only"
    This work is not validated for clinical decision-making. Clinical variant interpretation should be performed by qualified professionals using applicable ACMG/AMP and gene- or disease-specific guidance.

[View selected work](02_selected_work.md){ .md-button }
[Discuss collaboration](07_cv_contact.md){ .md-button .md-button--primary }
