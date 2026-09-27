---
title: "アクセシビリティ"
description: "アクセシビリティの基準と使い方。モバイルアプリ開発のスキル評価・チーム改善ガイド。"
---

# アクセシビリティ

**スキルID：** `mobile.accessibility`  
**スキル領域：** [応用基礎領域](index.md)  
**対象プラットフォーム：** 共通  
**主な前提：** UI実装、UIデザイン原則

[習熟度の共通定義と判定方法](../../guide/individual-assessment.md)に沿って、根拠を確認します。

## このスキルについて

目が見えにくい、指先を細かく動かしにくい、色の区別がつきにくいといった、さまざまな利用者がアプリを使えるようにするための設計と実装を扱うスキルです。スマートフォンには画面の内容を音声で読み上げる機能や文字を大きくする設定が OS に組み込まれており、アプリがその仕組みに正しく情報を渡すことで初めて役に立ちます。最初に押さえるのは、画面上の各要素に読み上げ用の名前（ラベル）と役割を付けることと、文字サイズを大きくしても表示が崩れないようにすることです。

分からない用語は[用語集](../../guide/glossary.md)で確認できます。

## Lv0

画面の読み上げ、文字サイズの変更、色の識別、タッチ領域の大きさなどに関する利用上の障壁を説明できず、基本的な確認に手順ごとの指示が必要である。

## Lv1

チェックリストに沿って要素のラベル、読み上げの順序、文字サイズを大きくしたときの表示を確認し、支援を受けて基本的な不備を修正できる。

## Lv2

チームの品質基準に沿って画面を実装し、検査ツールと読み上げ機能による確認を行える。要素の役割と状態、十分なタッチ領域、文字拡大時のレイアウト、入力エラーの伝達を検証できる。

## Lv3

独自の部品、ジェスチャ操作、動的な更新、モーダルの読み上げ順序とフォーカスを設計できる。検査ツールで検出できない障壁や動きを減らす設定への対応も調査し、代替案を比較してレビュー・修正できる。

## Lv4

対象範囲と適合目標、共通UI部品、自動検査と手動確認の手順、例外管理、教育を一体で整備できる。利用者による確認やチームの運用実績を基に、障壁の解消と継続的な品質維持を進められる。

## 次のLvへ進むために

学習の目安として、次の段階に進むための課題と参考資料を示します。課題は評価の条件ではありません。

| 目標 | 取り組む課題の例 | 参考資料 |
| :--- | :--- | :--- |
| Lv1 | 自分のアプリの1画面で読み上げ機能（VoiceOver または TalkBack）を有効にして操作し、ラベルのないボタンや読み上げ順序のおかしい箇所を記録して、支援を受けながら修正する | [Accessibility（Apple）](https://developer.apple.com/documentation/accessibility)・[アクセシビリティ（Android）](https://developer.android.com/guide/topics/ui/accessibility)・[アクセシビリティ（React Native）](https://reactnative.dev/docs/accessibility) |
| Lv2 | ログイン画面を作り、すべての入力欄とボタンにラベルと役割を付け、入力エラーを読み上げで伝える。文字サイズを最大にした状態と検査ツールで確認し、タッチ領域の不足を修正する | [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines)・[Material Design 3](https://m3.material.io/)・[アクセシビリティ（Android）](https://developer.android.com/guide/topics/ui/accessibility)・[アクセシビリティ（React Native）](https://reactnative.dev/docs/accessibility) |
| Lv3 | スワイプで削除する一覧や独自のスライダーなど、標準部品にない操作を読み上げ機能でも使えるようにする。モーダルを開いたときのフォーカス移動と、動きを減らす設定への対応を設計し、代替の操作手段を比較する | [Accessibility（Apple）](https://developer.apple.com/documentation/accessibility)・[アクセシビリティ（Android）](https://developer.android.com/guide/topics/ui/accessibility)・[アクセシビリティ（React Native）](https://reactnative.dev/docs/accessibility) |

## 技術の対応

| 用途 | iOS | Android | React Native |
| :--- | :--- | :--- | :--- |
| 画面の読み上げ | VoiceOver、accessibilityLabel／Traits | TalkBack、contentDescription | accessibilityLabel／Role、accessible |
| 文字サイズの変更 | Dynamic Type | フォントスケール | allowFontScaling、PixelRatio.getFontScale |
| 操作のしやすさ | 44pt以上のタップ領域（HIG） | タッチターゲット（48dp以上） | hitSlop、accessibilityRole |
| 動きの抑制と設定の取得 | Reduce Motion | システムのアニメーション設定 | AccessibilityInfo |
| 検査ツール | Accessibility Inspector | Accessibility Scanner | 各OSのツール（Accessibility Inspector／Scanner） |

roadmap.sh で学ぶ：[iOS](https://roadmap.sh/ios)（Accessibility、VoiceOver、Dynamic Type、Accessibility Inspector）／[SwiftUI](https://roadmap.sh/swift-ui)（Accessibility）／[React Native](https://roadmap.sh/react-native)（Accessibility）

## 評価を記録する

[個人のスキル評価書式](../../templates/individual-assessment.md)に、現在の判定、根拠、支援と制約、次の到達条件を記録します。
