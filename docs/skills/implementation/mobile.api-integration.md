---
title: "API連携とデータフロー"
description: "API連携とデータフローの基準と使い方。モバイルアプリ開発のスキル評価・チーム改善ガイド。"
---

# API連携とデータフロー

**スキルID：** `mobile.api-integration`  
**スキル領域：** [フレームワーク・実装領域](index.md)  
**対象プラットフォーム：** 共通  
**主な前提：** ネットワーク通信、データ永続化

[習熟度の共通定義と判定方法](../../guide/individual-assessment.md)に沿って、根拠を確認します。

## Lv0

APIの要求・応答、端末内の保存、画面表示の間でデータがどう流れるかを説明できず、実装に手順ごとの指示が必要である。

## Lv1

用意されたAPIクライアントとデータ取得層の例に沿って、データを取得し画面に表示できる。失敗時の扱いや保存方法は支援を受けて実装できる。

## Lv2

データ取得層を通じてAPIと端末内の保存を組み合わせ、読み込み中、空データ、失敗、認証切れを画面で扱える。認証情報を安全な保管場所に置き、オフラインや通信が不安定な状態でも動作を検証・修正できる。

## Lv3

キャッシュの有効期限、再試行とバックオフ、トークン更新の競合、ページ分割、オフライン時の更新と同期を設計できる。古いアプリ版との互換性を考慮し、バックエンドとエラー契約やデータ形式を調整できる。

## Lv4

共通のAPIクライアント、認証・再試行・エラー処理、キャッシュ方針とその検証方法を整備できる。他者の利用を支援し、連携不具合や仕様変更時の手戻りの減少を確認できる。

## 技術の対応

| プラットフォーム | 主な技術・API |
| :--- | :--- |
| iOS | Repository 層、キャッシュ方針、再試行・バックオフ、認証トークンの保管（Keychain）と更新、オフライン時の振る舞い、Codable の互換性 |
| Android | Repository + Room キャッシュ、Retrofit Interceptor（認証・再試行）、Paging、Result 型 |
| React Native | TanStack Query、SWR、fetch ラッパー、トークン保管（SecureStore） |

roadmap.sh の参照トピック：ios: rest, graphql, networking, keychain / android: authentication, network, repository-pattern / react-native: authentication, networking, storage

## 評価を記録する

[個人のスキル評価書式](../../templates/individual-assessment.md)に、現在の判定、根拠、支援と制約、次の到達条件を記録します。
