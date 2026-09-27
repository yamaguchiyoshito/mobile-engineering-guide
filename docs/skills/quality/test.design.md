---
title: "テスト設計"
description: "テスト設計の基準と使い方。モバイルアプリ開発のスキル評価・チーム改善ガイド。"
---

# テスト設計

**スキルID：** `test.design`  
**スキル領域：** [品質・高度化領域](index.md)  
**対象プラットフォーム：** 共通  
**主な前提：** 各テスト実装

[習熟度の共通定義と判定方法](../../guide/individual-assessment.md)に沿って、根拠を確認します。

## このスキルについて

アプリの要求や仕様を読み、何を、どの条件で、どのように確かめるかを決める技術です。モバイルアプリは機種、画面サイズ、OSバージョン、通信状態、権限の許可・拒否など動作を左右する条件がWebやサーバーより多く、すべての組み合わせを試すことはできないため、確かめる範囲と優先順位を意図して選ぶ必要があります。最初に押さえるのは、1つのテストケースを「前提条件・操作・期待結果」に分けて書くことと、正常な操作だけでなく入力の境界や失敗したときの動きも観点に含めることです。

分からない用語は[用語集](../../guide/glossary.md)で確認できます。

## Lv0

テストの観点、条件、手順、期待結果を区別できず、要求から検証内容を考えるために手順ごとの指示が必要である。

## Lv1

提供された観点と書式に沿ってケースを作成し、前提条件、入力、操作、期待結果を記述できる。仕様の読み取りと漏れの確認には支援が必要である。

## Lv2

要求と仕様から正常系、異常系、境界値、状態遷移を整理し、根拠のある期待結果と再現可能な手順を定義できる。検証を担当するテスト層を選び、不明な仕様を判断待ちとして分離できる。

## Lv3

機能横断、権限、データ整合性、例外、非機能リスクに加え、端末とOSバージョンの組み合わせを分析し、ケースの不足・重複をレビューできる。制約の中で優先順位と組み合わせを決め、未検証の範囲と残るリスクを説明できる。

## Lv4

リスク分析、観点抽出、仕様との対応付け、ケース記述、レビューの標準と支援ツールを整備できる。他者の設計結果と流出不具合を分析し、ケース数だけに依存しない網羅性と設計効率の改善を進められる。

## 次のLvへ進むために

学習の目安として、次の段階に進むための課題と参考資料を示します。課題は評価の条件ではありません。

| 目標 | 取り組む課題の例 | 参考資料 |
| :--- | :--- | :--- |
| Lv1 | 既存アプリのログイン画面について、用意された観点表に沿って前提条件・入力・操作・期待結果を持つテストケースを10件程度書き、シミュレータ・エミュレータまたは実機で手順どおりに実行して結果を記録する | [テスト（Android）](https://developer.android.com/training/testing)・[テストの概要（React Native）](https://reactnative.dev/docs/testing-overview) |
| Lv2 | 文字数制限と必須項目がある会員登録画面の仕様から、正常系・異常系・境界値・画面の状態遷移を整理したケース表を作り、各ケースを単体テスト・UIテスト・手動確認のどれで検証するかを割り当てる。仕様から判断できない点は質問事項として分けて書き出す | [XCTest](https://developer.apple.com/documentation/xctest)・[テスト（Android）](https://developer.android.com/training/testing)・[テストの概要（React Native）](https://reactnative.dev/docs/testing-overview) |
| Lv3 | 既存アプリの1機能について、権限の拒否、通信の切断、データの不整合、OSバージョンと画面サイズの違いを含むリスクを洗い出し、既存ケースの不足と重複をレビューする。優先順位と実行する端末の組み合わせを決め、未検証の範囲と残るリスクを文書にまとめる | [Xcode](https://developer.apple.com/documentation/xcode)・[テスト（Android）](https://developer.android.com/training/testing)・[Firebase Test Lab](https://firebase.google.com/docs/test-lab) |

## 技術の対応

| 用途 | iOS | Android | React Native |
| :--- | :--- | :--- | :--- |
| テストの種類と役割分担 | Xcode Test Plan | テスト種別（Local／Instrumented） | Jest／Detox の役割分担 |
| 網羅状況の確認 | カバレッジ（Xcode） | カバレッジ（JaCoCo） | カバレッジ（Jest） |
| 実行する端末・環境の範囲 | 端末・OS マトリクス | 端末マトリクス、Test Lab | Expo 環境でのテスト範囲 |

roadmap.sh で学ぶ：[iOS](https://roadmap.sh/ios)（Test Plan & Coverage、Unit & UI Testing）／[SwiftUI](https://roadmap.sh/swift-ui)（Testing）／[Android](https://roadmap.sh/android)（Testing）／[React Native](https://roadmap.sh/react-native)（Testing）

## 評価を記録する

[個人のスキル評価書式](../../templates/individual-assessment.md)に、現在の判定、根拠、支援と制約、次の到達条件を記録します。
