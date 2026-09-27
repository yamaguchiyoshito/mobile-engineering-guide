---
title: "CI/CD・静的解析"
description: "CI/CD・静的解析の基準と使い方。モバイルアプリ開発のスキル評価・チーム改善ガイド。"
---

# CI/CD・静的解析

**スキルID：** `mobile.cicd`  
**スキル領域：** [品質・高度化領域](index.md)  
**対象プラットフォーム：** 共通  
**主な前提：** チーム開発、ビルドと依存管理

[習熟度の共通定義と判定方法](../../guide/individual-assessment.md)に沿って、根拠を確認します。

## Lv0

継続的インテグレーション、自動ビルド、静的解析、自動配布の目的と違いを説明できず、パイプラインの結果確認に手順ごとの指示が必要である。

## Lv1

既存のパイプラインを実行し、失敗したジョブのログから該当箇所を確認できる。静的解析の指摘は支援を受けて修正できる。

## Lv2

変更ごとにビルド、静的解析、書式検査、単体テストを実行するワークフローを構成し、失敗時に原因を特定して修正できる。依存関係とビルド成果物のキャッシュを設定し、実行時間と結果を確認できる。

## Lv3

複数プラットフォームのビルド、署名情報の安全な受け渡し、UIテスト、配布までを含むパイプラインを設計できる。実行環境の費用と待ち時間、不安定なジョブ、静的解析規則の過不足を分析し、段階の分割や並列化で改善できる。

## Lv4

共通のパイプライン定義、静的解析と書式の規約、署名管理、失敗時の対応手順をチームの標準として整備できる。他者の利用実績を基に、ビルド時間、不安定な失敗、レビューでの指摘件数、リリースまでのリードタイムが改善したことを確認できる。

## 技術の対応

| プラットフォーム | 主な技術・API |
| :--- | :--- |
| iOS | fastlane、Xcode Cloud、GitHub Actions（macOS ランナー）、SwiftLint、SwiftFormat、署名の CI 管理（match 等） |
| Android | GitHub Actions、Bitrise、Gradle キャッシュ、ktlint、detekt、Android Lint |
| React Native | EAS Build のCI連携、ESLint／TypeScript 検査、Jest の CI 実行、Detox の CI 実行 |

roadmap.sh の参照トピック：ios: ci--cd, fastlane, github-actions, circleci, jenkins, azure-devops, code-quality-tools, swiftlint, swiftformat, tailor / android: linting, ktlint, detekt / react-native: development-workflow, speeding-up-builds

## 評価を記録する

[個人のスキル評価書式](../../templates/individual-assessment.md)に、現在の判定、根拠、支援と制約、次の到達条件を記録します。
