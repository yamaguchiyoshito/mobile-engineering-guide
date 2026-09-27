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

## このスキルについて

アプリのコードを書き、ビルドして端末で動かし、不具合を調べるための開発環境の使い方を扱います。Webであればブラウザを開けば動作を確認できますが、モバイルアプリはiOSならXcode、AndroidならAndroid Studio、React NativeならExpoなどの専用ツールでビルドし、パソコン上で端末を再現するシミュレータ・エミュレータや、接続した実機にインストールして動作を確認します。シミュレータ・エミュレータと実機では性能やカメラなどのセンサーの有無が異なるため、両方で確認する場面があります。最初に押さえるのは、プロジェクト、ターゲット（モジュール）、ビルド構成の関係と、ブレークポイントで処理を止めて変数の値を確かめるデバッガーの使い方です。

分からない用語は[用語集](../../guide/glossary.md)で確認できます。

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

## 次のLvへ進むために

学習の目安として、次の段階に進むための課題と参考資料を示します。課題は評価の条件ではありません。

| 目標 | 取り組む課題の例 | 参考資料 |
| :--- | :--- | :--- |
| Lv1 | 公式の手順に沿って新規プロジェクトを作成し、シミュレータ・エミュレータと実機の両方で起動する。ボタンを押したときの処理にブレークポイントを置き、変数の値とログを確認する | [Xcode](https://developer.apple.com/documentation/xcode)・[Android Studio](https://developer.android.com/studio)・[環境構築（React Native）](https://reactnative.dev/docs/environment-setup) |
| Lv2 | サンプルアプリに画面を1つ追加し、あらかじめ仕込んだ表示崩れや計算の誤りを、ステップ実行、ログ、画面構造の検査機能を使って見つけて修正する | [Xcode](https://developer.apple.com/documentation/xcode)・[Android Studio](https://developer.android.com/studio)・[Expo ドキュメント](https://docs.expo.dev/) |
| Lv3 | 実機でのみ起きる不具合（権限、性能、センサーなど）を題材に、シミュレータ・エミュレータとの差を切り分ける調査手順を書き、他の人が同じ手順で再現できるかを確かめる | [アプリ性能の改善](https://developer.apple.com/documentation/xcode/improving-your-app-s-performance)・[Android Studio](https://developer.android.com/studio)・[パフォーマンス（React Native）](https://reactnative.dev/docs/performance) |

## 技術の対応

| 用途 | iOS | Android | React Native |
| :--- | :--- | :--- | :--- |
| プロジェクトの構成 | Xcode プロジェクト・ターゲット・スキーム | Android Studio、Gradleモジュール構成 | Expo CLI、Metro |
| 端末での実行と変更の反映 | Simulator | Emulator、AVD | Fast Refresh |
| 処理の追跡とログ | ブレークポイント、Debug Navigator | Logcat | 開発者メニュー、LogBox |
| 画面の編集と構造の検査 | Interface Builder | Layout Inspector | React DevTools |
| ドキュメントの作成 | DocC | KDoc、Dokka | TSDoc、JSDoc |

roadmap.sh で学ぶ：[iOS](https://roadmap.sh/ios)（Xcode、Project Files、Interface Builder、Breakpoints、Debug Navigator、Stepping、Xcode Debugger、Debugging Techniques）／[SwiftUI](https://roadmap.sh/swift-ui)（Xcode、Xcode Debugging、Swift Playgrounds、DocC）／[Android](https://roadmap.sh/android)（Development IDE、Debugging、Create a Basic Hello World App）／[React Native](https://roadmap.sh/react-native)（Environment Setup、Metro Bundler、DevTools、In-App Developer Menu、LogBox、Enabling Fast Refresh、Running on Device）

## 評価を記録する

[個人のスキル評価書式](../../templates/individual-assessment.md)に、現在の判定、根拠、支援と制約、次の到達条件を記録します。
