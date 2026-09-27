---
title: "API連携とデータフロー"
description: "API連携とデータフローの基準と使い方。モバイルアプリ開発の習熟度評価・チーム改善ガイド。"
---

# API連携とデータフロー

**要素技術ID：** `mobile.api-integration`  
**技術領域：** [フレームワーク・実装領域](index.md)  
**対象プラットフォーム：** 共通  
**主な前提：** ネットワーク通信、データ永続化

[習熟度の共通定義と判定方法](../../guide/individual-assessment.md)に沿って、根拠を確認します。

## この要素技術について

サーバーのAPIから受け取ったデータを、端末内の保存領域と組み合わせて画面に届けるまでの流れを設計・実装する技術です。モバイルアプリは移動中に通信が途切れやすく、利用者が古い版のアプリを使い続けることもあるため、通信の失敗、ログインの期限切れ、データ形式の変更を前提に作る必要があります。最初に押さえるのは、画面がAPIを直接呼ばずにデータ取得を受け持つ層（Repository）を通すことと、読み込み中・データなし・失敗・認証切れという画面の状態を区別して扱うことです。

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
| Lv1 | 公開されているAPIからデータを取得して一覧に表示するアプリを公式の手順に沿って作り、機内モードにして通信に失敗したときの表示を確認する | [Foundation](https://developer.apple.com/documentation/foundation)・[ネットワーク接続](https://developer.android.com/training/basics/network-ops)・[ネットワーク（React Native）](https://reactnative.dev/docs/network) |
| Lv2 | APIから取得した一覧を端末に保存し、次回起動時や通信できないときは保存済みのデータを表示するアプリを作る。読み込み中・空・失敗の表示と、認証トークンの安全な保存を実装する | [Keychain Services](https://developer.apple.com/documentation/security/keychain-services)・[Room](https://developer.android.com/training/data-storage/room)・[Retrofit](https://github.com/square/retrofit)・[セキュリティ（React Native）](https://reactnative.dev/docs/security) |
| Lv3 | 複数の通信が同時に認証切れになったとき、トークンの更新を1回だけ行って元の通信をやり直す仕組みを設計する。再試行の間隔を段階的に延ばす処理とページ分割の読み込みを加え、通信を遅くした環境で検証する | [アプリアーキテクチャガイド](https://developer.android.com/topic/architecture)・[Swift Concurrency](https://developer.apple.com/documentation/swift/concurrency)・[OWASP MAS](https://mas.owasp.org/) |

## 技術の対応

| 用途 | iOS | Android | React Native |
| :--- | :--- | :--- | :--- |
| データ取得の層 | Repository層 | Repository | fetchラッパー |
| キャッシュとページ分割 | キャッシュ方針、オフライン時の振る舞い | Roomキャッシュ、Paging | TanStack Query、SWR |
| 認証トークン | 認証トークンの保管（Keychain）と更新 | Retrofit Interceptor（認証） | トークン保管（SecureStore） |
| 再試行とエラー処理 | 再試行・バックオフ | Retrofit Interceptor（再試行）、Result型 | TanStack Queryのretry、エラー境界 |
| データ形式の互換性 | Codableの互換性 | kotlinx.serializationの既定値・未知項目の扱い | zodなどによる実行時検証 |

## 関連ライブラリと参考資料

主な一次情報の所在です。掲載は公式資料と、技術の対応表に挙げた広く使われるライブラリに限ります。採用を推奨するものではありません。

<!-- references:start ids="urlsession, urlcache, keychain-services, codable, android-data-layer, android-room, android-paging, retrofit, kotlinx-serialization, kotlin-result, rn-network, tanstack-query, swr, expo-securestore, zod" -->

| 種別 | 名称 | 対象 | 概要 |
| :--- | :--- | :--- | :--- |
| 公式リファレンス | [URLSession](https://developer.apple.com/documentation/foundation/urlsession) | iOS | HTTPリクエストの送信と応答の受信を行うiOS標準のAPI |
| 公式リファレンス | [URLCache](https://developer.apple.com/documentation/foundation/urlcache) | iOS | URLリクエストへの応答をメモリやディスクに保存する仕組み |
| 公式リファレンス | [Keychain Services](https://developer.apple.com/documentation/security/keychain-services) | iOS | パスワードやトークンなどの秘密情報を暗号化して保存するAPI |
| 公式リファレンス | [Codable](https://developer.apple.com/documentation/swift/codable) | iOS | JSONなどの外部表現と型の間でデータを相互に変換するプロトコル |
| 公式リファレンス | [Room](https://developer.android.com/training/data-storage/room) | Android | SQLiteをオブジェクトとして扱えるようにするデータベースのライブラリ |
| 公式リファレンス | [Paging](https://developer.android.com/topic/libraries/architecture/paging/v3-overview) | Android | 大きなデータを分割して読み込み表示するJetpackライブラリ |
| 公式リファレンス | [Result](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-result/) | Android | 処理の成功値または例外を1つの値で表すKotlinの型 |
| 公式リファレンス | [Networking（React Native）](https://reactnative.dev/docs/network) | React Native | fetchでのHTTP通信とWebSocketの使い方を説明するページ |
| ライブラリ | [Retrofit](https://github.com/square/retrofit) | Android | インターフェースの定義からHTTP APIの呼び出し処理を生成するライブラリ |
| ライブラリ | [kotlinx.serialization](https://github.com/Kotlin/kotlinx.serialization) | Android | KotlinのクラスとJSONなどの形式を相互に変換するライブラリ |
| ライブラリ | [TanStack Query](https://tanstack.com/query/latest) | React Native | サーバーから取得したデータのキャッシュと再取得を管理するライブラリ |
| ライブラリ | [SWR](https://github.com/vercel/swr) | React Native | キャッシュを返しつつ再検証してデータを取得するReactフック |
| ライブラリ | [SecureStore](https://docs.expo.dev/versions/latest/sdk/securestore/) | React Native | 端末の安全な保存領域にキーと値を暗号化して保存するライブラリ |
| ライブラリ | [Zod](https://zod.dev/) | React Native | スキーマを定義して実行時にデータの形式を検証するライブラリ |
| 学習資料 | [Data layer](https://developer.android.com/topic/architecture/data-layer) | Android | Repositoryでデータの取得元をまとめるデータ層の設計指針 |

<!-- references:end -->

roadmap.shで学ぶ：[iOS](https://roadmap.sh/ios)（REST、GraphQL、Networking、Keychain）／[Android](https://roadmap.sh/android)（Authentication、Network、Repository pattern）／[React Native](https://roadmap.sh/react-native)（Authentication、Networking、Storage）

## 評価を記録する

[個人の習熟度評価書式](../../templates/individual-assessment.md)に、現在の判定、根拠、支援と制約、次の到達条件を記録します。
