---
title: "開発環境（Xcode／Android Studio／Expo）"
description: "開発環境（Xcode／Android Studio／Expo）の基準と使い方。モバイルアプリ開発のスキル評価・チーム改善ガイド。"
---

# 開発環境（Xcode／Android Studio／Expo）

**スキルID：** `ide.basic`  
**スキル領域：** [基礎領域](index.md)  
**対象プラットフォーム：** 共通  
**評価対象：** プロジェクト構成、ビルド実行、デバッガ、シミュレータ・エミュレータ

[習熟度の共通定義と判定方法](../../guide/individual-assessment.md)に沿って、根拠を確認します。

## Lv0

プロジェクト、ターゲットやモジュール、ビルド構成の関係を説明できず、ビルドやアプリの起動に手順ごとの指示が必要である。

## Lv1

手順書に沿ってプロジェクトを開き、シミュレータ・エミュレータや実機でアプリをビルド・実行できる。指定された箇所にブレークポイントを設定し、変数の値やログを確認できる。

## Lv2

プロジェクト構成を理解してファイルや画面を追加し、通常のビルドエラーを自力で解消できる。ステップ実行、ログ、画面構造の検査機能を使って不具合の箇所を特定し、修正後の動作を確認できる。

## Lv3

実機でのみ再現する不具合、複数の構成や端末にまたがる問題、開発環境自体の不調などを切り分け、原因を分析できる。調査手段を組み合わせて調査手順を設計し、他者の調査を支援・レビューできる。

## Lv4

開発環境の構築手順、推奨設定、デバッグ手順、演習をチームで再現できる形に整備できる。他者の利用実績から、環境構築や不具合調査にかかる時間の変化を確認し、仕組みを更新できる。

## 技術の対応

| プラットフォーム | 主な技術・API |
| :--- | :--- |
| iOS | Xcode プロジェクト・ターゲット・スキーム、Interface Builder、ブレークポイント、Debug Navigator、Simulator、DocC |
| Android | Android Studio、Gradleモジュール構成、Logcat、Layout Inspector、Emulator、AVD |
| React Native | Expo CLI、Metro、Fast Refresh、開発者メニュー、LogBox、React DevTools |

roadmap.sh の参照トピック：ios: xcode, project-files, interface-builder, interface-overview, breakpoints, debug-navigator, stepping, xcode-debugger, debugging-techniques, new-project / android: development-ide, debugging, create-a-basic-hello-world-app / react-native: environment-setup, metro-bundler, devtools, in-app-developer-menu, logbox, enabling-fast-refresh, running-on-device / swift-ui: xcode, xcode-debugging, swift-playgrounds, docc

## 評価を記録する

[個人のスキル評価書式](../../templates/individual-assessment.md)に、現在の判定、根拠、支援と制約、次の到達条件を記録します。
