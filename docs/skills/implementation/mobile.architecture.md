---
title: "アプリアーキテクチャと依存性注入"
description: "アプリアーキテクチャと依存性注入の基準と使い方。モバイルアプリ開発のスキル評価・チーム改善ガイド。"
---

# アプリアーキテクチャと依存性注入

**スキルID：** `mobile.architecture`  
**スキル領域：** [フレームワーク・実装領域](index.md)  
**対象プラットフォーム：** 共通  
**主な前提：** UI実装、リアクティブプログラミング

[習熟度の共通定義と判定方法](../../guide/individual-assessment.md)に沿って、根拠を確認します。

## Lv0

画面、状態、データ取得の責務の違いや依存関係の向きを説明できず、既存構成への機能追加にも手順ごとの指示が必要である。

## Lv1

既存のアーキテクチャに沿って、指定された層に画面や処理を追加できる。依存の注入やテスト用の差し替えは例に従って実装できる。

## Lv2

要件が明確な機能を表示層、状態を持つ層、データ層に分け、依存性注入で結合を切り離して実装できる。層ごとの責務を守ってユニットテストを書き、通常の機能追加と修正を完了できる。

## Lv3

画面の規模、チームの人数、テストのしやすさ、ビルド時間などの制約から、アーキテクチャパターンやモジュール分割を比較・選択できる。層の越境や循環依存を分析し、既存構成を段階的に改善して他者の設計をレビューできる。

## Lv4

アーキテクチャの方針、ひな形、依存ルールの自動検査を整備し、チームで再現できる構成にできる。他者の利用と移行を支援し、変更の影響範囲や実装工数の改善を確認して方針を更新できる。

## 技術の対応

| プラットフォーム | 主な技術・API |
| :--- | :--- |
| iOS | MVC、MVVM、MVVM-C、VIPER、TCA、Clean Architecture、Swift のDI（イニシャライザ注入、Environment、Factory）、モジュール分割（SPM） |
| Android | MVVM、MVI、Repository パターン、UseCase、Hilt／Dagger、Koin、Kodein、マルチモジュール |
| React Native | コンテナ・プレゼンテーション分離、状態管理ライブラリ（Redux、Zustand）、Context による注入 |

roadmap.sh の参照トピック：ios: architectural-patterns, mvc, mvp, mvvm, mvvm-c, viper, tca, combine-and-mvvm, rxswift-with-mvvm, functional-programming / android: design--architecture, mvc, mvp, mvvm, mvi, repository-pattern, builder-pattern, factory-pattern, dependency-injection, hilt, dagger, koin, kodein / swift-ui: app-architecture, mvvm, clean-architecture, dependency-injection

## 評価を記録する

[個人のスキル評価書式](../../templates/individual-assessment.md)に、現在の判定、根拠、支援と制約、次の到達条件を記録します。
