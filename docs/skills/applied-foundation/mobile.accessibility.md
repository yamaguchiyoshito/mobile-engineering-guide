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

## 技術の対応

| プラットフォーム | 主な技術・API |
| :--- | :--- |
| iOS | VoiceOver、Dynamic Type、accessibilityLabel／Traits、Accessibility Inspector、Reduce Motion |
| Android | TalkBack、contentDescription、タッチターゲット、Accessibility Scanner、フォントスケール |
| React Native | accessibilityLabel／Role、accessible、AccessibilityInfo |

roadmap.sh の参照トピック：ios: accessibility, voice-over, dynamic-type, accessibility-inspector / swift-ui: accessibility / react-native: accessibility

## 評価を記録する

[個人のスキル評価書式](../../templates/individual-assessment.md)に、現在の判定、根拠、支援と制約、次の到達条件を記録します。
