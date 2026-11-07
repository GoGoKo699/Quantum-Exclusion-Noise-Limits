# Actual GitHub rendering checks

The hosted collector opens exact public commit-pinned GitHub Markdown pages in a fresh unsigned Chromium context. It does not inject styles or render the source inside the page. All tracked Markdown pages are covered by default, at widths 1440 and 760 pixels. Local MathJax compilation supplies only the expected MathML structure; actual GitHub MathML, text and screenshots supply the observed side.

## Reproduce

Use Node.js 22, Python 3.10 or newer, Git and a supported browser environment. The CI workflow pins Ubuntu 24.04. Install temporary dependencies outside the source checkout, then run from its root:

```sh
npm install --prefix /tmp/exclusion-browser playwright@1.56.1 mathjax-full@3.2.1
/tmp/exclusion-browser/node_modules/.bin/playwright install --with-deps chromium
python verification/hosted/build_contract.py --root . --repository GoGoKo699/Quantum-Exclusion-Noise-Limits --revision FULL_COMMIT_SHA --output /tmp/exclusion-contract.json
NODE_PATH=/tmp/exclusion-browser/node_modules node verification/hosted/capture_hosted_math.cjs --root . --repository GoGoKo699/Quantum-Exclusion-Noise-Limits --revision FULL_COMMIT_SHA --contract /tmp/exclusion-contract.json --output /tmp/exclusion-hosted
```

Replace `FULL_COMMIT_SHA` with the inspected full 40-character commit. Use new output paths. The contract binds four headline expressions to required visible operands and labels. The collector compares every inventoried expression structurally, checks expression counts and relation symbols, and flags rendering banners, missing operands, and collapsed or overflowing displays. It retains source hashes, HTML, screenshots, capture/check files and `hosted-report.json`. A failed report remains failed until the affected source is repaired and recaptured.

The workflow has only `contents: read`, disables persisted checkout credentials, and installs browser dependencies in the runner's temporary directory. It exports verification evidence as a short-lived artifact. No public result or readiness claim should depend on an expired artifact alone; retain the relevant report and revision evidence separately when needed.

## Interpretation

A passing automated report does not establish visual readability or scientific correctness. Inspect the screenshots of the principal claims, proofs and learning pages at both widths, including every repaired expression, against the exact source. The check observes one renderer version and does not guarantee future GitHub behavior or every browser.

The generic collector and scanner are kept together in `verification/hosted/`; their source versions are identified by their Git blob hashes in the repository. The project-specific contract adds content checks without disabling the structural comparison. Technical dependency and network failures are distinct from access or administrator-policy denials. No alternative account or network route may be used to bypass a denial.
