---
title: "ユニットテスト"
description: "ユニットテストの基準と使い方。モバイルアプリ開発のスキル評価・チーム改善ガイド。"
---

# ユニットテスト

**スキルID：** `test.unit`  
**スキル領域：** [品質・高度化領域](index.md)  
**対象プラットフォーム：** 共通  
**主な前提：** Swift、Kotlin、またはTypeScript

[習熟度の共通定義と判定方法](../../guide/individual-assessment.md)に沿って、根拠を確認します。

## Lv0

テスト対象、入力、期待結果、アサーションの関係を説明できず、テストの追加、実行、失敗原因の確認に個別の指示が必要である。

## Lv1

既存例に沿って関数や型の正常系テストを追加し、開発環境またはコマンドで実行して結果を確認できる。失敗時は支援を受けて入力・期待結果・実装を照合できる。

## Lv2

責務と仕様から、正常系、境界値、空値、エラーのテストを実装し、成功・失敗の両方でテストが意図どおり反応することを確認できる。通信や永続化などの外部依存をテストダブルで分離し、非同期処理の完了を待って結果を検証できる。

## Lv3

状態保持、並行処理、時刻、プラットフォーム機能への依存を含むコードを、依存の注入や境界の分離で検証可能な構造にできる。過度なモック、実装内部への依存、実行順や時刻で結果が変わるテストを見つけ、検出力と保守性を保って改善できる。

## Lv4

単体テストの対象選定、記述規約、テストダブルと非同期検証の共通補助、CIでの実行と保守の仕組みを整備できる。チームの不具合事例とテスト変更工数を分析し、実行速度・検出力・保守性が改善したことを利用実績で確認できる。

## 技術の対応

| プラットフォーム | 主な技術・API |
| :--- | :--- |
| iOS | XCTest、Swift Testing、テストダブル、非同期テスト（async／await、expectation） |
| Android | JUnit、MockK、kotlinx-coroutines-test、Turbine（Flow） |
| React Native | Jest、React Native Testing Library、react-test-renderer、モジュールモック |

roadmap.sh の参照トピック：ios: xctest / swift-ui: swift-testing, xctest / android: junit / react-native: jest, react-native-testing-library, react-test-renderer

## 評価を記録する

[個人のスキル評価書式](../../templates/individual-assessment.md)に、現在の判定、根拠、支援と制約、次の到達条件を記録します。
