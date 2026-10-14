---
title: "valueOf"
---

```kotlin
open fun valueOf(name: String): AbstractPack.PackType
```

Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)

#### Return

the enum constant with the specified name

#### Throws

| | |
|---|---|
| [java.lang.IllegalArgumentException](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/IllegalArgumentException.html) | if this enum type has no constant with the specified name |
