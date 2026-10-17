---
title: "write"
---

```kotlin
abstract fun write()
```

A method that writes **all** data to disk.

Since that data can be different, this method is meant to be implemented by the extending class.

Example data would be [writeMetadata](/docs/api/mods/potion_totems/potion_totems/pack/abstract-pack/write-metadata/)**and must be included, otherwise Minecraft will not recognise the pack!**

#### Throws

| |
|---|
| [java.io.IOException](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/io/IOException.html) |
