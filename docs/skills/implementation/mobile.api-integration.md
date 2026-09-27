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

## このスキルについて

サーバーの API から受け取ったデータを、端末内の保存領域と組み合わせて画面に届けるまでの流れを設計・実装する技術です。モバイルアプリは移動中に通信が途切れやすく、利用者が古い版のアプリを使い続けることもあるため、通信の失敗、ログインの期限切れ、データ形式の変更を前提に作る必要があります。最初に押さえるのは、画面が API を直接呼ばずにデータ取得を受け持つ層（Repository）を通すことと、読み込み中・データなし・失敗・認証切れという画面の状態を区別して扱うことです。

分からない用語は[用語集](../../guide/glossary.md)で確認できます。

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

## 次のLvへ進むために

学習の目安として、次の段階に進むための課題と参考資料を示します。課題は評価の条件ではありません。

| 目標 | 取り組む課題の例 | 参考資料 |
| :--- | :--- | :--- |
| Lv1 | 公開されている API からデータを取得して一覧に表示するアプリを公式の手順に沿って作り、機内モードにして通信に失敗したときの表示を確認する | [Foundation](https://developer.apple.com/documentation/foundation)・[ネットワーク接続](https://developer.android.com/training/basics/network-ops)・[ネットワーク（React Native）](https://reactnative.dev/docs/network) |
| Lv2 | API から取得した一覧を端末に保存し、次回起動時や通信できないときは保存済みのデータを表示するアプリを作る。読み込み中・空・失敗の表示と、認証トークンの安全な保存を実装する | [Keychain Services](https://developer.apple.com/documentation/security/keychain-services)・[Room](https://developer.android.com/training/data-storage/room)・[Retrofit](https://github.com/square/retrofit)・[セキュリティ（React Native）](https://reactnative.dev/docs/security) |
| Lv3 | 複数の通信が同時に認証切れになったとき、トークンの更新を1回だけ行って元の通信をやり直す仕組みを設計する。再試行の間隔を段階的に延ばす処理とページ分割の読み込みを加え、通信を遅くした環境で検証する | [アプリアーキテクチャガイド](https://developer.android.com/topic/architecture)・[Swift Concurrency](https://developer.apple.com/documentation/swift/concurrency)・[OWASP MAS](https://mas.owasp.org/) |

## 技術の対応

| 用途 | iOS | Android | React Native |
| :--- | :--- | :--- | :--- |
| データ取得の層 | Repository 層 | Repository | fetch ラッパー |
| キャッシュとページ分割 | キャッシュ方針、オフライン時の振る舞い | Room キャッシュ、Paging | TanStack Query、SWR |
| 認証トークン | 認証トークンの保管（Keychain）と更新 | Retrofit Interceptor（認証） | トークン保管（SecureStore） |
| 再試行とエラー処理 | 再試行・バックオフ | Retrofit Interceptor（再試行）、Result 型 | TanStack Query の retry、エラー境界 |
| データ形式の互換性 | Codable の互換性 | kotlinx.serialization の既定値・未知項目の扱い | zod などによる実行時検証 |

roadmap.sh で学ぶ：[iOS](https://roadmap.sh/ios)（REST、GraphQL、Networking、Keychain）／[Android](https://roadmap.sh/android)（Authentication、Network、Repository pattern）／[React Native](https://roadmap.sh/react-native)（Authentication、Networking、Storage）

## 評価を記録する

[個人のスキル評価書式](../../templates/individual-assessment.md)に、現在の判定、根拠、支援と制約、次の到達条件を記録します。
