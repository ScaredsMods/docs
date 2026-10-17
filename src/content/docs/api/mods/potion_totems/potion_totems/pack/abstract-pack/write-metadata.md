---
title: "writeMetadata"
---

```kotlin
open fun writeMetadata()
```

This method is used for writing the pack.mcmeta file characterising the pack.

This doesn't really need to be changed, as the format is pretty much the same for basic resource and datapacks, it doesn't need to be implemented.

**This method must be called in** [**write**](/docs/api/mods/potion_totems/potion_totems/pack/abstract-pack/write/)**, otherwise Minecraft will not recognise the pack!**

#### Throws

| |
|---|
| [java.io.IOException](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/io/IOException.html) |
