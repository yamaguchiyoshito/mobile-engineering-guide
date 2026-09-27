---
title: "画面遷移とディープリンク"
description: "画面遷移とディープリンクの基準と使い方。モバイルアプリ開発のスキル評価・チーム改善ガイド。"
---

# 画面遷移とディープリンク

**スキルID：** `mobile.navigation`  
**スキル領域：** [フレームワーク・実装領域](index.md)  
**対象プラットフォーム：** 共通  
**主な前提：** UI実装

[習熟度の共通定義と判定方法](../../guide/individual-assessment.md)に沿って、根拠を確認します。

## Lv0

画面の積み重ね、モーダル、タブの違いと戻る操作の挙動を説明できず、画面遷移の追加に手順ごとの指示が必要である。

## Lv1

既存例に沿って画面を追加し、引数を渡して遷移する処理と戻る処理を実装できる。指定された操作手順で遷移結果を確認できる。

## Lv2

階層、モーダル、タブを組み合わせた通常の画面遷移を実装し、戻る操作と画面状態の保持を扱える。URLから特定の画面を開く処理を実装し、未起動時と起動中の両方で検証・修正できる。

## Lv3

認証状態による分岐、深い階層への直接遷移、プロセス再生成後の復元、多重遷移などの例外を設計できる。遷移の責務をアーキテクチャに組み込み、不整合の原因を分析して他者の実装をレビューできる。

## Lv4

遷移の定義方法、リンクの仕様、遷移の自動検証を整備できる。他者の利用と画面追加を支援し、遷移不具合やリンク切れの減少を確認して仕組みを更新できる。

## 技術の対応

| プラットフォーム | 主な技術・API |
| :--- | :--- |
| iOS | NavigationStack／UINavigationController、モーダル、TabView、Universal Links、URL Scheme、Coordinator |
| Android | Navigation Component、バックスタックと Task、Intent Filter、App Links、App Shortcuts、Predictive Back |
| React Native | React Navigation（Stack／Tab／Drawer）、Expo Router、Linking |

roadmap.sh の参照トピック：ios: navigation, navigators, navigation-stacks, modals-and-navigation, view-transitions, modals / android: tasks--backstack, intent-filters, app-shortcuts, navigation-components / react-native: screen-navigation, deeplinking

## 評価を記録する

[個人のスキル評価書式](../../templates/individual-assessment.md)に、現在の判定、根拠、支援と制約、次の到達条件を記録します。
