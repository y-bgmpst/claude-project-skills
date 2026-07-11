# Release and Versioning

This repository does not need a heavy release process, but it benefits from a predictable one.

## Versioning approach

Use simple semantic versioning for the repo as a whole when you publish a release:

- major: incompatible layout or workflow change
- minor: new skills or new helper tooling
- patch: documentation fixes or small metadata corrections

## What a release should capture

A release should describe:

- what skills were added or changed
- whether installers changed
- whether the validator changed
- whether any workflow assumptions changed

## Recommended release flow

1. merge the relevant PRs to `main`
2. create a release branch only if you need a staging pass
3. generate a release draft with a concise summary
4. verify the install helper and validation output
5. publish the release

## Release notes should include

- new or changed skill names
- breaking changes to skill layout
- any changes to the install path or validator behavior
- any changes to CI coverage

## Draft release checklist

Before publishing a release draft, make sure:

- `main` is green
- the skills install correctly
- the wiki reflects the current repo layout
- the PR template still matches the actual contribution workflow

## When to skip a release

Skip a formal release if the change is only:

- wiki text
- a typo fix
- a small metadata alignment fix

In that case, a merged PR is enough.
