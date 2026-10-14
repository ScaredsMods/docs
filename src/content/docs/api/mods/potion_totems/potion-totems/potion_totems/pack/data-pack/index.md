---
title: "DataPack"
sidebar:
  label: "Overview"
---

[java]\
open class [DataPack](/docs/api/mods/potion_totems/potion-totems/potion_totems/pack/data-pack/) : [AbstractPack](/docs/api/mods/potion_totems/potion-totems/potion_totems/pack/abstract-pack/)

## Constructors

| | |
|---|---|
| [DataPack](/docs/api/mods/potion_totems/potion-totems/potion_totems/pack/data-pack/data-pack/) | [java]<br>constructor(name: [String](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html), description: [String](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html), packFormat: [Array](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html)&lt;[Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)&gt;, minPackFormat: [Array](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html)&lt;[Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)&gt;, maxPackFormat: [Array](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html)&lt;[Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)&gt;) |

## Properties

| Name | Summary |
|---|---|
| [description](/docs/api/mods/potion_totems/potion-totems/potion_totems/pack/abstract-pack/description/) | [java]<br>val [description](/docs/api/mods/potion_totems/potion-totems/potion_totems/pack/abstract-pack/description/): [String](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html) |
| [GSON](/docs/api/mods/potion_totems/potion-totems/potion_totems/pack/abstract-pack/g-s-o-n/) | [java]<br>val [GSON](/docs/api/mods/potion_totems/potion-totems/potion_totems/pack/abstract-pack/g-s-o-n/): Gson |
| [maxPackFormat](/docs/api/mods/potion_totems/potion-totems/potion_totems/pack/abstract-pack/max-pack-format/) | [java]<br>val [maxPackFormat](/docs/api/mods/potion_totems/potion-totems/potion_totems/pack/abstract-pack/max-pack-format/): [Array](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html)&lt;[Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)&gt; |
| [minPackFormat](/docs/api/mods/potion_totems/potion-totems/potion_totems/pack/abstract-pack/min-pack-format/) | [java]<br>val [minPackFormat](/docs/api/mods/potion_totems/potion-totems/potion_totems/pack/abstract-pack/min-pack-format/): [Array](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html)&lt;[Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)&gt; |
| [name](/docs/api/mods/potion_totems/potion-totems/potion_totems/pack/abstract-pack/name/) | [java]<br>val [name](/docs/api/mods/potion_totems/potion-totems/potion_totems/pack/abstract-pack/name/): [String](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html) |
| [packFormat](/docs/api/mods/potion_totems/potion-totems/potion_totems/pack/abstract-pack/pack-format/) | [java]<br>val [packFormat](/docs/api/mods/potion_totems/potion-totems/potion_totems/pack/abstract-pack/pack-format/): [Array](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html)&lt;[Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)&gt; |

## Functions

| Name | Summary |
|---|---|
| [getPath](/docs/api/mods/potion_totems/potion-totems/potion_totems/pack/abstract-pack/get-path/) | [java]<br>open fun [getPath](/docs/api/mods/potion_totems/potion-totems/potion_totems/pack/abstract-pack/get-path/)(): [Path](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/nio/file/Path.html) |
| [write](/docs/api/mods/potion_totems/potion-totems/potion_totems/pack/data-pack/write/) | [java]<br>open fun [write](/docs/api/mods/potion_totems/potion-totems/potion_totems/pack/data-pack/write/)() |
| [writeMetadata](/docs/api/mods/potion_totems/potion-totems/potion_totems/pack/abstract-pack/write-metadata/) | [java]<br>open fun [writeMetadata](/docs/api/mods/potion_totems/potion-totems/potion_totems/pack/abstract-pack/write-metadata/)() |
| [writePackIcon](/docs/api/mods/potion_totems/potion-totems/potion_totems/pack/data-pack/write-pack-icon/) | [java]<br>open fun [writePackIcon](/docs/api/mods/potion_totems/potion-totems/potion_totems/pack/data-pack/write-pack-icon/)(modId: [String](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html)) |
