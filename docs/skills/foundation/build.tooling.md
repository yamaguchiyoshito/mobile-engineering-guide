---
title: "ビルドと依存管理"
description: "ビルドと依存管理の基準と使い方。モバイルアプリ開発のスキル評価・チーム改善ガイド。"
---

# ビルドと依存管理

**スキルID：** `build.tooling`  
**スキル領域：** [基礎領域](index.md)  
**対象プラットフォーム：** 共通  
**評価対象：** ビルド設定、依存関係の追加・更新、成果物の生成

[習熟度の共通定義と判定方法](../../guide/individual-assessment.md)に沿って、根拠を確認します。

## Lv0

ビルド設定、依存関係、成果物の関係を説明できず、ライブラリの追加やビルドに手順ごとの指示が必要である。

## Lv1

手順書に沿って依存ライブラリを追加し、指定された構成でビルドして成果物を生成できる。依存の競合やビルド設定の変更が必要な場合に支援を求められる。

## Lv2

要件に合わせて依存ライブラリを選定・追加・更新し、開発用とリリース用などのビルド構成を使い分けられる。ビルドエラーや依存の不整合を解消し、生成した成果物が意図した構成であることを確認できる。

## Lv3

推移的な依存の競合、更新による互換性の破壊、ビルド時間の増大などを分析し、原因を特定して改善できる。依存の導入可否やモジュール分割の案を保守性、ビルド時間、成果物サイズの観点で比較し、他者の変更をレビューできる。

## Lv4

依存管理とビルド構成の標準、共通設定、依存更新の自動検証を整備できる。他者の利用実績から、ビルド失敗や依存更新にかかる工数の変化を確認し、仕組みを更新できる。

## 技術の対応

| プラットフォーム | 主な技術・API |
| :--- | :--- |
| iOS | Swift Package Manager、CocoaPods、Carthage、xcframework、ビルド設定（Configuration）、xcodebuild |
| Android | Gradle（Kotlin DSL）、バージョンカタログ、Build Variant、R8、署名付きAPK／AAB |
| React Native | npm／yarn、Expo プレビルド、EAS Build、autolinking、Hermes |

roadmap.sh の参照トピック：ios: swift-package-manager, cocoapods, carthage, dependency-manager, xcframework, static-library, dynamic-library, frameworks--library / android: what-is-and-how-to-use-gradle, signed-apk / react-native: expo, react-native-cli, create-expo-app, speeding-up-builds / swift-ui: creating-packages, using-packages, swift-package-index

## 評価を記録する

[個人のスキル評価書式](../../templates/individual-assessment.md)に、現在の判定、根拠、支援と制約、次の到達条件を記録します。
