---
title: "React Native実装"
description: "React Native実装の基準と使い方。モバイルアプリ開発のスキル評価・チーム改善ガイド。"
---

# React Native実装

**スキルID：** `react-native.basic`  
**スキル領域：** [フレームワーク・実装領域](index.md)  
**対象プラットフォーム：** React Native  
**主な前提：** JavaScript、TypeScript、React（[フロントエンド開発ガイド](https://github.com/YOUR_OWNER/frontend-engineering-guide)を参照）

[習熟度の共通定義と判定方法](../../guide/individual-assessment.md)に沿って、根拠を確認します。

## このスキルについて

React Native は、Web の React と同じコンポーネント、props、state の考え方で画面を組み立てながら、HTML と CSS ではなく iOS と Android のネイティブの画面部品を描いてアプリを作る仕組みです。そのため div や span の代わりに View や Text などのコアコンポーネントを使い、スタイルも CSS ファイルではなく JavaScript のオブジェクトで指定します。開発の進め方には、環境構築や実機での確認、ストア配布用のビルドを代行する基盤である Expo を使う方法と、Xcode と Android Studio のネイティブプロジェクトを直接扱う Bare の方法があります。Expo で用意されていない端末機能を使うとき、ネイティブ側のビルドエラーを調べるとき、ストア配布の設定を変えるときには、iOS と Android それぞれの知識が必要になります。最初に押さえるのは、コアコンポーネントと props／state の関係と、同じコードでも iOS と Android で見た目や挙動が異なる場合があることです。

分からない用語は[用語集](../../guide/glossary.md)で確認できます。

## Lv0

コアコンポーネント、props、stateと画面表示の関係を説明できず、単純な画面の変更にも手順ごとの指示が必要である。

## Lv1

例や支援に沿ってコアコンポーネントとスタイルを組み合わせ、テキスト、画像、ボタン、一覧を表示できる。指定された端末やシミュレーターで表示と操作を確認できる。

## Lv2

要件が明確な画面をコンポーネントに分け、状態更新、入力、スクロール、一覧、モーダルを実装できる。iOSとAndroidの両方で表示と操作を検証し、プラットフォーム間の差異を自分で修正できる。

## Lv3

一覧の再描画、JSスレッドの負荷、端末ごとの表示差異に起因する不具合を分析できる。複雑な画面の構成と部品の分割を設計し、Web向けReactとの違いを踏まえて他者の実装をレビューできる。

## Lv4

共通コンポーネント、スタイルの規約、プロジェクト構成、実機での検証基準を整備できる。他者の利用と更新対応を支援し、同種不具合や画面実装工数の改善を確認できる。

## 次のLvへ進むために

学習の目安として、次の段階に進むための課題と参考資料を示します。課題は評価の条件ではありません。

| 目標 | 取り組む課題の例 | 参考資料 |
| :--- | :--- | :--- |
| Lv1 | 公式ドキュメントまたは Expo の手順に沿ってプロジェクトを作り、Text、Image、Pressable、FlatList を使った一覧画面をシミュレーターと実機で表示する | [はじめに](https://reactnative.dev/docs/getting-started)・[コアコンポーネント](https://reactnative.dev/docs/intro-react-native-components)・[Expo ドキュメント](https://docs.expo.dev/) |
| Lv2 | 一覧・詳細・追加の3画面を持つ ToDo アプリを作り、TextInput での入力、モーダルでの確認、スクロールを実装する。iOS と Android の両方で動かし、見た目や挙動の差を Platform による分岐で直す | [スタイル](https://reactnative.dev/docs/style)・[Flexbox](https://reactnative.dev/docs/flexbox)・[プラットフォーム固有コード](https://reactnative.dev/docs/platform-specific-code) |
| Lv3 | 数百件を表示する FlatList のスクロールがかくつく状態を再現し、再描画の原因を調べて改善する。Web 向け React の書き方がそのまま持ち込まれている既存コードをレビューし、修正点をまとめる | [パフォーマンス（React Native）](https://reactnative.dev/docs/performance)・[コアコンポーネント](https://reactnative.dev/docs/intro-react-native-components) |

## 技術の対応

| 用途 | 主な技術・API |
| :--- | :--- |
| 画面の部品 | View、Text、Image、Modal |
| 一覧とスクロール | ScrollView、FlatList、SectionList |
| 入力と操作 | TextInput、Pressable |
| スタイル | StyleSheet |
| 状態と部品の分割 | props／state、Hooks |
| 開発と確認 | Expo SDK、Expo Snack、Fast Refresh |

roadmap.sh で学ぶ：[React Native](https://roadmap.sh/react-native)（Core components、Props、State、FlatList、Text input、Pressable、Modal、Expo Snack）

## 評価を記録する

[個人のスキル評価書式](../../templates/individual-assessment.md)に、現在の判定、根拠、支援と制約、次の到達条件を記録します。
