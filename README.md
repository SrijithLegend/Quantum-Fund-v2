# Quantum Fund v2

### Event-Driven Pre-Market Intelligence Engine for Alpha Discovery

---

## Overview

**Quantum Fund v2** is a next-generation, event-driven equity intelligence system designed to identify high-probability intraday opportunities *before market open*.

Unlike traditional technical indicators that react to price, Quantum Fund v2 operates on **information asymmetry**, aggregating pre-market signals such as institutional activity, sentiment shifts, and order flow imbalances to forecast directional moves.

This system is built to capture **early-stage momentum** driven by capital flows and news catalysts, rather than chasing lagging confirmations.

---

## Core Architecture

```text
Data Ingestion Layer
        ↓
Signal Extraction Layer
        ↓
Feature Engineering Pipeline
        ↓
Event Scoring Engine
        ↓
Ranking & Filtering System
        ↓
Final Trade Candidates (Top N)
```

---

## Key Features

### 1. Pre-Market Intelligence Engine

* Processes **pre-market data** to identify early directional bias
* Captures **gap dynamics**, overnight sentiment shifts, and liquidity positioning
* Enables **front-running of intraday momentum**

---

### 2. Institutional Flow Detection

* Integrates **Bulk Deals & Block Deals**
* Detects:

  * Accumulation patterns
  * Large capital deployments
  * Strategic positioning by institutions

---

### 3. Short Selling Pressure Analysis

* Monitors **short-selling activity and intensity**
* Identifies:

  * Potential short squeezes
  * Bearish conviction zones
* Incorporates into directional scoring logic

---

### 4. News Sentiment Engine

* Real-time parsing of financial news streams
* NLP-based sentiment classification:

  * Positive (earnings beats, contracts, approvals)
  * Negative (downgrades, regulatory risks, losses)
* Weighted impact based on:

  * Recency
  * Frequency
  * Keyword intensity

---

### 5. Event-Based Scoring Model

Each stock is evaluated using a composite **Event Momentum Score (0–100)**:

| Component          | Description                           |
| ------------------ | ------------------------------------- |
| Pre-Market Bias    | Gap + early positioning               |
| Institutional Flow | Bulk/block deal intensity             |
| Short Interest     | Short pressure / squeeze probability  |
| News Sentiment     | Event-driven catalysts                |
| Liquidity Profile  | Tradability and execution feasibility |

---

### 6. Intelligent Ranking Engine

* Multi-factor scoring system
* Prioritizes:

  * High-impact catalysts
  * Institutional confirmation
  * Liquidity + execution feasibility
* Outputs **Top N high-conviction trade candidates**

---

## Strategy Philosophy

> **Price follows information. Institutions act before price confirms.**

Quantum Fund v2 is built on the principle that:

* **Events → Flows → Price**
* Retail traders lose by reacting late
* Alpha exists in **early detection of intent**

---

## Output Format

Example output:

```text
Stock        Signal   Score   PreMkt   Inst Flow   Short   Sentiment
--------------------------------------------------------------------
HFCL         BUY      87      Strong   High        Low     Positive
MTARTECH     BUY      82      Gap-Up   Medium      Low     Positive
SYNGENE      BUY      79      Neutral  High        Medium  Positive
CEMPRO       BUY      76      Gap-Up   High        Low     Positive
```

---

## Tech Stack

* **Python**
* **yfinance** (market data ingestion)
* **Custom NSE Data Parsers** (bulk/block deals)
* **Pandas / NumPy** (data processing)
* **Rule-Based + Heuristic Scoring Models**
* **Modular Indicator Architecture**

---

## Design Principles

* **Latency-aware**: focuses on early signals, not delayed confirmations
* **Modular**: plug-and-play indicators
* **Explainable**: every signal is traceable
* **Execution-focused**: prioritizes tradable setups

---

## Limitations

* Dependent on data availability and quality
* News sentiment is heuristic (not full NLP model yet)
* No guarantee of profitability — this is a decision-support system

---

## Roadmap

* [ ] Real-time data pipeline (WebSocket integration)
* [ ] ML-based sentiment classification
* [ ] Reinforcement learning for adaptive weighting
* [ ] Portfolio-level risk optimization
* [ ] Broker API integration for auto-execution

---

## Disclaimer

This project is for **educational and research purposes only**.
It does not constitute financial advice. Use at your own risk.

---

## Author

**Quantum Fund System v2**
Built for high-performance intraday intelligence and event-driven trading.

---
