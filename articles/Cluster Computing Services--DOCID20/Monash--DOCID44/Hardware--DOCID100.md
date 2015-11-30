# MonARCH Hardware Summary

There are two classes of compute nodes on MonARCH. They are broken into "High
Speed" and "High Core Count" flavours.

* config A: high-ish CPU clock speed, lower-core count, standard RAM

  * 16 physical cores or 32 HT cores ==> two Intel Xeon E5-2667 v3 3.2GHz, 20M
    Cache, 9.60GT/s QPI, Turbo, HT, 8C/16T (135W)
  * 128 GB RAM == 8 x 16GB RDIMM, 2133 MT/s, Dual Rank, x4 Data Width

* config B: lower CPU clock speed, high-core count, higher RAM

  * 24 physical cores or 48 HT cores ==> two Intel Xeon E5-2680 v3 2.5GHz, 30M
    Cache, 9.60GT/s QPI, Turbo, HT, 12C/24T (120W)
  * 256 GB RAM == 16 x 16GB RDIMM, 2133 MT/s, Dual Rank, x4 Data Width
