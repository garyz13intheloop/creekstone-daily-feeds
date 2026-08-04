# ClawHub Skills Daily | 2026-08-04

> 共 25 个 skills

## [1. geoskill-climate-downscaling](https://clawhub.ai/ruiduobao/geoskill-climate-downscaling)

**Slug**: `geoskill-climate-downscaling`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 统计降尺度：用多元回归建立粗分辨率气候变量与高分辨率地形预测因子的关系，并对残差做空间插值，生成高分辨率气候栅格

**中文介绍**: 统计降尺度：用多元回归建立粗分辨率气候变量与高分辨率地形预测因子的关系，并对残差做空间插值，生成高分辨率气候栅格

Latest changelog:
Initial release — statistical downscaling for climate data:

- Implements "terrain regression + residual spatial interpolation" for converting coarse-resolution climate variables to high-resolution rasters.
- Supports both real data (multi-band GeoTIFF input) and fully offline synthesized scenarios.
- Outputs include high-resolution downscaled raster, regression/residual component stack, and validation report (correlation, RMSE, lapse rate, improvements).
- Fully local workflow; no network or data upload required.
- English and Chinese usage documentation provided.

**关键词**: 统计降尺度, 并对残差做空间插值, 生成高分辨率气候栅格, Latest, changelog, Initial, release, statistical

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/geoskill-climate-downscaling)

---

## [2. geoskill-change-detection-dl](https://clawhub.ai/ruiduobao/geoskill-change-detection-dl)

**Slug**: `geoskill-change-detection-dl`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Siamese 全卷积网络(FC-Siam-diff 风格)双时相变化检测：GPU 训练/推理，输出变化概率、二值变化图与变化图斑

**中文介绍**: Siamese 全卷积网络(FC-Siam-diff 风格)双时相变化检测：GPU 训练/推理，输出变化概率、二值变化图与变化图斑

Latest changelog:
- Initial release of geoskill-change-detection-dl.
- Provides deep learning-based land surface change detection from bi-temporal imagery using a Siamese fully convolutional network (FC-Siam-diff style).
- Outputs include change probability maps, binary change maps, and change-region polygons in GeoJSON format.
- Supports GPU-accelerated training and inference; includes pretrained weights (with automatic on-GPU training if weights are missing).
- Handles both synthetic and real imagery inputs; all processing is local and offline by default.

**关键词**: 全卷积网络, 风格, 双时相变化检测, 训练, 推理, Siamese, FC-Siam-diff, GPU

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/geoskill-change-detection-dl)

---

## [3. geoskill-carbon-stock-estimation](https://clawhub.ai/ruiduobao/geoskill-carbon-stock-estimation)

**Slug**: `geoskill-carbon-stock-estimation`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 由 NDVI 幂律异速生长方程估算地上生物量碳，叠加根茎比地下碳与类型化土壤碳密度。Estimates carbon stocks from biomass allometry and soil carbon density. 输出地上碳/土壤碳/总碳三张 GeoTIFF 与汇总 JSON。

**中文介绍**: 由 NDVI 幂律异速生长方程估算地上生物量碳，叠加根茎比地下碳与类型化土壤碳密度。Estimates carbon stocks from biomass allometry and soil carbon density. 输出地上碳/土壤碳/总碳三张 GeoTIFF 与汇总 JSON。

Latest changelog:
geoskill-carbon-stock-estimation 1.0.0

- First public release: estimates aboveground, belowground, and soil carbon stocks from NDVI and classified land cover.
- Generates three GeoTIFF outputs (aboveground, soil, total carbon) plus summary and manifest JSON.
- Supports both synthetic data generation and real NDVI raster input.
- Exposes user-tunable parameters for allometric scale/power and root-to-shoot ratio.
- Fully local/offline processing; no network access or data uploads.
- Provides detailed limitations and underlying data source explanation (transparently in both Chinese and English).

**关键词**: 幂律异速生长方程估算地上生物量碳, 叠加根茎比地下碳与类型化土壤碳密度, NDVI, Estimates, carbon, stocks, biomass, allometry

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/geoskill-carbon-stock-estimation)

---

## [4. geoskill-carbon-flux-estimation](https://clawhub.ai/ruiduobao/geoskill-carbon-flux-estimation)

**Slug**: `geoskill-carbon-flux-estimation`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 基于光能利用率模型（CASA/VPM 简化）估算 GPP/NPP：GPP=PAR×FPAR×ε，ε 受温度与水分胁迫调节，NPP=GPP−自养呼吸，输出碳收支

**中文介绍**: 基于光能利用率模型（CASA/VPM 简化）估算 GPP/NPP：GPP=PAR×FPAR×ε，ε 受温度与水分胁迫调节，NPP=GPP−自养呼吸，输出碳收支

Latest changelog:
- Initial release of geoskill-carbon-flux-estimation.
- Estimates ecosystem carbon fluxes (GPP, NPP, autotrophic respiration) using a simplified light-use-efficiency model (CASA/VPM-style).
- Supports both synthetic (offline, automatic field generation) and real input (multi-band GeoTIFF for PAR, FPAR, temperature, water) modes.
- Outputs cumulative GPP/NPP GeoTIFF rasters, daily flux time series and carbon budget JSON, and manifest.
- Runs offline by default with all processing done locally; no data upload required.
- Documentation included in both English and Chinese.

**关键词**: 基于光能利用率模型（CASA, 简化）估算, 受温度与水分胁迫调节, NPP=GPP−自养呼吸, VPM, GPP, NPP, GPP=PAR×FPAR×ε

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/geoskill-carbon-flux-estimation)

---

## [5. geoskill-building-density-mapping](https://clawhub.ai/ruiduobao/geoskill-building-density-mapping)

**Slug**: `geoskill-building-density-mapping`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Estimate building footprint density and floor area ratio (FAR) from building footprints and heights using kernel density estimation.

**中文介绍**: Estimate building footprint density and floor area ratio (FAR) from building footprints and heights using kernel density estimation.

Latest changelog:
Initial release of geoskill-building-density-mapping.

- Estimates building density (coverage ratio) and floor area ratio (FAR) from raster building footprints and heights using kernel density estimation.
- Provides both command line usage for local TIFF data and an offline synthetic data mode.
- Outputs GeoTIFF with two bands (building density, FAR), along with JSON statistics and a run manifest.
- All processing is performed locally with no network or data upload; suitable for privacy-sensitive scenarios.
- Open source under the MIT license.

**关键词**: Estimate, building, footprint, density, floor, area, ratio, FAR

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/geoskill-building-density-mapping)

---

## [6. geoskill-biodiversity-mapping](https://clawhub.ai/ruiduobao/geoskill-biodiversity-mapping)

**Slug**: `geoskill-biodiversity-mapping`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 基于生境异质性假说，用 NDVI 生产力、纹理结构异质性与地形粗糙度三类代理估算物种丰富度空间分布。Maps species richness proxies from NDVI, texture and terrain heterogeneity. 输出物种丰富度与生境质量 GeoTIFF + 参数 JSON。

**中文介绍**: 基于生境异质性假说，用 NDVI 生产力、纹理结构异质性与地形粗糙度三类代理估算物种丰富度空间分布。Maps species richness proxies from NDVI, texture and terrain heterogeneity. 输出物种丰富度与生境质量 GeoTIFF + 参数 JSON。

Latest changelog:
Initial release: Maps spatial species richness proxies from NDVI, texture, and terrain heterogeneity with flexible offline operation.

- Calculates species richness using normalized NDVI productivity, local NDVI texture, and DEM-derived terrain heterogeneity as proxies
- Supports both real multispectral GeoTIFF inputs and fully offline synthetic data
- Outputs habitat quality and species richness as GeoTIFFs, plus a parameters JSON and manifest
- Offers two weighting schemes (heterogeneity, productivity) for proxy fusion and multiple configuration options
- Runs entirely offline by default; no user data is uploaded or sent externally

**关键词**: 基于生境异质性假说, NDVI, Maps, species, richness, proxies, texture, terrain

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/geoskill-biodiversity-mapping)

---

## [7. geoskill-bathymetry-estimation](https://clawhub.ai/ruiduobao/geoskill-bathymetry-estimation)

**Slug**: `geoskill-bathymetry-estimation`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 用 Stumpf 对数比值或 Lyzenga 线性变换从蓝绿波段反演浅海水深，含校准与精度评估

**中文介绍**: 用 Stumpf 对数比值或 Lyzenga 线性变换从蓝绿波段反演浅海水深，含校准与精度评估

Latest changelog:
geoskill-bathymetry-estimation v1.0.0

- Initial release with bathymetry estimation using Stumpf log-ratio or Lyzenga linear blue-green algorithms.
- Supports calibration, accuracy evaluation, and both synthetic and real-world usage modes.
- Outputs GeoTIFF and JSON manifest files.
- All processing is local and privacy-friendly; synthetic mode is fully offline.
- Includes example commands and installation instructions.

**关键词**: 对数比值或, 线性变换从蓝绿波段反演浅海水深, 含校准与精度评估, v1.0.0, Stumpf, Lyzenga, Latest, changelog

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/geoskill-bathymetry-estimation)

---

## [8. geoskill-bare-soil-mapping](https://clawhub.ai/ruiduobao/geoskill-bare-soil-mapping)

**Slug**: `geoskill-bare-soil-mapping`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 融合裸土指数 BSI、亮度与局部纹理（裸土低对比度）阈值提取裸土/裸地分布，支持 Otsu 自动阈值，输出裸土 GeoTIFF、BSI 栅格与面积统计。Maps bare soil by fusing BSI, brightness and local texture.

**中文介绍**: 融合裸土指数 BSI、亮度与局部纹理（裸土低对比度）阈值提取裸土/裸地分布，支持 Otsu 自动阈值，输出裸土 GeoTIFF、BSI 栅格与面积统计。Maps bare soil by fusing BSI, brightness and local texture.

Latest changelog:
Initial release of geoskill-bare-soil-mapping.

- Maps bare soil by combining Bare Soil Index (BSI), brightness, and local texture, distinguishing it from vegetation, urban areas, and water.
- Supports automatic thresholding with the Otsu method or manual threshold settings.
- Outputs include bare soil mask GeoTIFF, BSI raster, area statistics (JSON), and run manifest.
- Works with both synthetic and user-provided multi-band imagery; all computation runs offline.
- Includes usage examples and full documentation in both English and Chinese.

**关键词**: 融合裸土指数, 裸地分布, 支持, 自动阈值, 输出裸土, 栅格与面积统计, Otsu, GeoTIFF、BSI

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/geoskill-bare-soil-mapping)

---

## [9. geoskill-band-ratio-analysis](https://clawhub.ai/ruiduobao/geoskill-band-ratio-analysis)

**Slug**: `geoskill-band-ratio-analysis`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 批量计算NDVI/NDWI/MNDWI/NDBI/EVI/SAVI等光谱指数，逐指数输出GeoTIFF与值域统计

**中文介绍**: 批量计算NDVI/NDWI/MNDWI/NDBI/EVI/SAVI等光谱指数，逐指数输出GeoTIFF与值域统计

Latest changelog:
geoskill-band-ratio-analysis 1.0.0

- Initial release with support for batch calculation of common spectral indices (NDVI, NDWI, MNDWI, NDBI, EVI, SAVI).
- Outputs individual GeoTIFF results and value range statistics for each index.
- Provides example commands for both synthetic offline data and real-world usage.
- Includes privacy guarantees: all processing is local, with optional fully offline mode.

**关键词**: SAVI等光谱指数, 逐指数输出GeoTIFF与值域统计, 批量计算NDVI, NDWI, MNDWI, NDBI, EVI, Latest

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/geoskill-band-ratio-analysis)

---

## [10. geoskill-archaeology-site-detection](https://clawhub.ai/ruiduobao/geoskill-archaeology-site-detection)

**Slug**: `geoskill-archaeology-site-detection`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: LiDAR micro-topography, multispectral anomaly and SAR fusion for suspected archaeological site detection with anomaly grading

**中文介绍**: LiDAR micro-topography, multispectral anomaly and SAR fusion for suspected archaeological site detection with anomaly grading

Latest changelog:
Initial release of geoskill-archaeology-site-detection.

- Detects suspected archaeological sites by fusing LiDAR (DEM), multispectral (NDVI), and SAR backscatter data.
- Supports both real multi-band GeoTIFF inputs and fully offline synthetic data generation.
- Provides adjustable fusion methods (weighted or maximum), anomaly grading (none/low/high), and output of results as GeoTIFF, GeoJSON, and JSON summary files.
- Runs fully offline by default; all processing and data remain local.
- Includes example usage for custom weights, thresholds, and processing windows.
- Licensed under MIT.

**关键词**: LiDAR, micro-topography, multispectral, anomaly, SAR, fusion, suspected, archaeological

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/geoskill-archaeology-site-detection)

---

## [11. geoskill-animated-map-series](https://clawhub.ai/ruiduobao/geoskill-animated-map-series)

**Slug**: `geoskill-animated-map-series`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Compose multi-temporal rasters into unified rendered frames and a GIF animation

**中文介绍**: Compose multi-temporal rasters into unified rendered frames and a GIF animation

Latest changelog:
- Initial release of geoskill-animated-map-series.
- Renders multi-epoch (multi-band GeoTIFF) rasters into per-frame PNGs with a unified color scale and composes looping GIFs.
- Supports offline synthetic data generation and various color mapping options.
- Produces animation GIFs, per-frame PNGs, a GeoTIFF stack, and frame statistics as JSON.
- Built-in privacy: all processing is local; no data uploads required.

**关键词**: Compose, multi-temporal, rasters, unified, rendered, frames, GIF, animation

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/geoskill-animated-map-series)

---

## [12. geoskill-air-quality-dispersion](https://clawhub.ai/ruiduobao/geoskill-air-quality-dispersion)

**Slug**: `geoskill-air-quality-dispersion`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 高斯烟羽模型模拟点源污染物浓度场，Pasquill-Gifford A-F 稳定度参数化 σy/σz，叠加 DEM 地形修正。Simulates pollutant concentration fields with a Gaussian plume model plus terrain correction. 输出浓度场 GeoTIFF + 参数 JSON。

**中文介绍**: 高斯烟羽模型模拟点源污染物浓度场，Pasquill-Gifford A-F 稳定度参数化 σy/σz，叠加 DEM 地形修正。Simulates pollutant concentration fields with a Gaussian plume model plus terrain correction. 输出浓度场 GeoTIFF + 参数 JSON。

Latest changelog:
- Initial release of geoskill-air-quality-dispersion.
- Simulates ground-level pollutant concentration fields using the Gaussian plume model, with Pasquill-Gifford/Briggs stability classes and terrain correction (DEM support).
- Outputs include GeoTIFF concentration fields and JSON parameter summaries.
- Supports fully offline operation, synthetic and DEM-based runs, and batch/silent modes.
- Documentation provided in both English and Chinese.

**关键词**: 高斯烟羽模型模拟点源污染物浓度场, A-F, 稳定度参数化, σy, σz, 叠加, Pasquill-Gifford, DEM

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/geoskill-air-quality-dispersion)

---

## [13. geoskill-ai-training-data-annotation](https://clawhub.ai/ruiduobao/geoskill-ai-training-data-annotation)

**Slug**: `geoskill-ai-training-data-annotation`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 小型 U-Net 二值语义分割 (torch+CUDA) 预标注 + 主动学习不确定性选样，输出 COCO/GeoJSON 标注与不确定性栅格

**中文介绍**: 小型 U-Net 二值语义分割 (torch+CUDA) 预标注 + 主动学习不确定性选样，输出 COCO/GeoJSON 标注与不确定性栅格

Latest changelog:
- Initial release of geoskill-ai-training-data-annotation.
- Provides a small U-Net model for binary semantic segmentation on remote sensing imagery using torch+CUDA.
- Supports automatic pre-annotation (pseudo-labeling), active learning uncertainty sampling, and outputs standard COCO/GeoJSON annotations as well as an uncertainty (entropy) raster.
- Includes pretrained weights and a classical Otsu thresholding baseline for GPU-free environments.
- Runs fully offline and processes data locally; synthetic data mode requires no network.

**关键词**: 小型, 二值语义分割, 预标注, 主动学习不确定性选样, 输出, U-Net, torch+CUDA, COCO

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/geoskill-ai-training-data-annotation)

---

## [14. geoskill-ai-report-generator](https://clawhub.ai/ruiduobao/geoskill-ai-report-generator)

**Slug**: `geoskill-ai-report-generator`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 分析结果JSON模板填充，生成结构化HTML/Markdown报告（离线numpy等价实现）

**中文介绍**: 分析结果JSON模板填充，生成结构化HTML/Markdown报告（离线numpy等价实现）

Latest changelog:
Initial release: generates AI-assisted remote sensing analysis reports offline using NumPy-equivalent logic.

- Converts analysis results (JSON/raster stats) into structured HTML/Markdown reports, including summary stats, detail tables, ratings, and conclusions.
- Fully offline operation; does not require LLMs or network access.
- All dynamic content is HTML-escaped for security.
- Outputs include HTML, Markdown, summary JSON, and run manifest files.
- Supports both English and Chinese usage documentation.

**关键词**: 分析结果JSON模板填充, 生成结构化HTML, Markdown报告（离线numpy等价实现）, Latest, changelog, Initial, release, generates

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/geoskill-ai-report-generator)

---

## [15. geoskill-ai-accuracy-assessment](https://clawhub.ai/ruiduobao/geoskill-ai-accuracy-assessment)

**Slug**: `geoskill-ai-accuracy-assessment`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 混淆矩阵+OA/mIoU/F1计算+空间精度图，输出精度评估报告（离线numpy等价实现）

**中文介绍**: 混淆矩阵+OA/mIoU/F1计算+空间精度图，输出精度评估报告（离线numpy等价实现）

Latest changelog:
Initial release providing offline, NumPy-based model accuracy assessment for classification and segmentation.

- Computes confusion matrix, overall accuracy (OA), mIoU, Cohen's Kappa, and per-class Precision/Recall/F1.
- Generates spatial accuracy maps showing local error distribution.
- Supports both synthetic data (with error blocks) and user-provided rasters.
- Outputs comprehensive accuracy report (JSON), spatial accuracy GeoTIFF, and manifest.
- Processes all data offline for privacy; no network required.

**关键词**: 混淆矩阵+OA, F1计算+空间精度图, 输出精度评估报告（离线numpy等价实现）, mIoU, Latest, changelog, Initial, release

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/geoskill-ai-accuracy-assessment)

---

## [16. geoskill-agriculture-subsidy-verification](https://clawhub.ai/ruiduobao/geoskill-agriculture-subsidy-verification)

**Slug**: `geoskill-agriculture-subsidy-verification`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 高分辨率作物识别叠加申报地块做差异检测，核查补贴合规性。Verifies subsidy compliance by overlaying high-resolution crop classification on declared parcels for difference detection.

**中文介绍**: 高分辨率作物识别叠加申报地块做差异检测，核查补贴合规性。Verifies subsidy compliance by overlaying high-resolution crop classification on declared parcels for difference detection.

Latest changelog:
Initial release – high-resolution remote sensing-based crop verification for subsidy compliance.

- Verifies per-parcel declared vs. measured crop fractions using NDVI data and vector parcel boundaries.
- Supports two verification methods: area difference (default) and class match.
- Outputs crop mask, parcel raster, per-parcel verification report, flagged parcels, and manifest.
- Handles NoData appropriately and does not flag parcels with no valid pixels.
- Works offline and never uploads user data; synthetic mode for offline simulation.
- Requires numpy, rasterio, geopandas, and shapely.

**关键词**: 高分辨率作物识别叠加申报地块做差异检测, 核查补贴合规性, Verifies, subsidy, compliance, overlaying, high-resolution, crop

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/geoskill-agriculture-subsidy-verification)

---

## [17. geoskill-3d-terrain-visualization](https://clawhub.ai/ruiduobao/geoskill-3d-terrain-visualization)

**Slug**: `geoskill-3d-terrain-visualization`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Render 3D terrain from DEM and imagery with vertical exaggeration and an HTML viewer

**中文介绍**: Render 3D terrain from DEM and imagery with vertical exaggeration and an HTML viewer

Latest changelog:
- Initial release of geoskill-3d-terrain-visualization.
- Renders 3D terrain from DEM and imagery with vertical exaggeration.
- Computes per-pixel normal vectors and Lambertian illumination for realistic lighting.
- Outputs a CSS 3D perspective HTML viewer with draggable pitch/rotation and exaggeration control.
- Supports both real GeoTIFF input and offline synthetic data generation.
- All processing is offline; no user data is uploaded.

**关键词**: 3D, an, Render, terrain, DEM, imagery, vertical, exaggeration

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/geoskill-3d-terrain-visualization)

---

## [18. geoskill-buffer-analysis](https://clawhub.ai/ruiduobao/geoskill-buffer-analysis)

**Slug**: `geoskill-buffer-analysis`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 矢量缓冲区生成+融合+叠加分析+面积统计

**中文介绍**: 矢量缓冲区生成+融合+叠加分析+面积统计

Latest changelog:
geoskill-buffer-analysis v1.0.0

- Initial release supporting vector buffer analysis for point, line, and polygon features.
- Includes buffer generation, merging (unary_union/dissolve), overlay analysis, and projected area statistics (km²).
- Provides offline synthetic data generation or real local input processing.
- Outputs buffers, dissolved buffers, statistics, and manifest files in GeoTIFF/GeoJSON/JSON formats.
- Fully offline operation; no data upload or network access required.
- Licensed under MIT.

**关键词**: 矢量缓冲区生成+融合+叠加分析+面积统计, v1.0.0, geoskill-buffer-analysis, Latest, changelog, Initial, release, supporting

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/geoskill-buffer-analysis)

---

## [19. Story Causal Engine](https://clawhub.ai/nohn3043-arch/story-engine-for-creator)

**Slug**: `story-engine-for-creator`  
**Version**: 1.1.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 3

**原始简介**: Craft epic tales anchored in deterministic causal reasoning.Every plot flaw comes to light; every timeline falls into seamless alignment; not a single logical fracture remains unaddressed in your world-building.Functioning as a second-perspective analytical engine, it audits narratives just as a seasoned detective dissects every shred of evidence.

**中文介绍**: Craft epic tales anchored in deterministic causal reasoning.Every plot flaw comes to light; every timeline falls into seamless alignment; not a single logical fracture remains unaddressed in your world-building.Functioning as a second-perspective analytical engine, it audits narratives just as a seasoned detective dissects every shred of evidence.

Latest changelog:
**English localization and rebranding, documentation update:**

- SKILL.md now fully translated from Chinese to English
- Display name changed from "创作者故事因果引擎" to "Story Causal Engine"
- Description and feature explanations rewritten for an international audience
- All usage instructions, examples, and scenarios are now in English
- No changes to core functionality or engine commands

**关键词**: Story, Causal, Engine, Craft, epic, tales, anchored, deterministic

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/story-engine-for-creator)

---

## [20. anthropomorphic-agent-engine](https://clawhub.ai/nohn3043-arch/anthropomorphic-agent-engine)

**Slug**: `anthropomorphic-agent-engine`  
**Version**: 1.1.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 3

**原始简介**: Breathe genuine life into AI agents with our deterministic psychology engine.Emotions span eight dimensions, surging and lingering naturally. Trauma leaves lasting imprints on memory. Trust gradually fades as interactions unfold.There are no opaque black boxes, no unregulated randomness. What emerges are reproducible personalities, brimming with tangible humanity.

**中文介绍**: Breathe genuine life into AI agents with our deterministic psychology engine.Emotions span eight dimensions, surging and lingering naturally. Trauma leaves lasting imprints on memory. Trust gradually fades as interactions unfold.There are no opaque black boxes, no unregulated randomness. What emerges are reproducible personalities, brimming with tangible humanity.

Latest changelog:
- English localization: SKILL.md rewritten fully in English with clearer, more concise descriptions.
- Improved documentation: core features, trigger scenarios, and usage examples now more clearly structured and explained.
- Modernized description: new summary highlights emotional modeling details and reproducibility.
- License and technical notes clarified and streamlined.
- No changes to code or core functionality—documentation update only.

**关键词**: Agent, Breathe, genuine, life, our, deterministic, psychology, engine.Emotions

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/anthropomorphic-agent-engine)

---

## [21. NOMOS Decision Hub](https://clawhub.ai/nohn3043-arch/nomos-decision-hub)

**Slug**: `nomos-decision-hub`  
**Version**: 1.2.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 4

**原始简介**: Every decision leaves a trail. NOMOS traces each choice to its causal roots, stress-tests assumptions until they break, and rebuilds rankings from the survivors — a deterministic decision engine where nothing is hidden and everything is auditable. Validated by Singapore IMDA AI Verify at 95/100.

**中文介绍**: Every decision leaves a trail. NOMOS traces each choice to its causal roots, stress-tests assumptions until they break, and rebuilds rankings from the survivors — a deterministic decision engine where nothing is hidden and everything is auditable. Validated by Singapore IMDA AI Verify at 95/100.

Latest changelog:
- Major update: English rewrite of documentation and user guidance.
- All core capabilities, usage instructions, and deterministic contract sections rewritten in English for broader accessibility.
- Descriptions updated for clarity, consistency, and improved onboarding.
- No functional/code changes—documentation and communication improvement only.

**关键词**: NOMOS, Decision, Hub, Every, leaves, trail, traces, each

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/nomos-decision-hub)

---

## [22. Maybeai Sheet Cli Skill](https://clawhub.ai/no7dw/maybeai-sheet-cli)

**Slug**: `maybeai-sheet-cli`  
**Version**: 0.19.1  
**Stats**: ⭐ 0 | ⬇️ 1058 | 🧩 26

**原始简介**: Inspect, import, edit, dashboard, template, and share MaybeAI spreadsheets

**中文介绍**: Inspect, import, edit, dashboard, template, and share MaybeAI spreadsheets

Latest changelog:
fix: forum calculate 加上save_result的参数

**关键词**: Maybeai, Sheet, Cli, Skill, Inspect, import, edit, dashboard

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/maybeai-sheet-cli)

---

## [23. RFC lookup](https://clawhub.ai/shbernal/rfc-lookup)

**Slug**: `rfc-lookup`  
**Version**: 0.2.4  
**Stats**: ⭐ 0 | ⬇️ 133 | 🧩 6

**原始简介**: Look up IETF RFCs and read what a specification actually says. Use whenever an RFC number comes up ("RFC 9110", "RFC 2616", "rfc7231"), when checking what a protocol spec requires, when quoting normative MUST/SHOULD/MAY language, when asked "what does the spec say about X", or when verifying whether an RFC is still current or has been obsoleted. Covers HTTP, TCP/IP, DNS, TLS, QUIC, SMTP, OAuth, JSON/JOSE and every other IETF standard. Finds the right RFC, reads one section instead of the whole document, and flags superseded specifications before they get cited.

**中文介绍**: Look up IETF RFCs and read what a specification actually says. Use whenever an RFC number comes up ("RFC 9110", "RFC 2616", "rfc7231"), when checking what a protocol spec requires, when quoting normative MUST/SHOULD/MAY language, when asked "what does the spec say about X", or when verifying whether an RFC is still current or has been obsoleted. Covers HTTP, TCP/IP, DNS, TLS, QUIC, SMTP, OAuth, JSON/JOSE and every other IETF standard. Finds the right RFC, reads one section instead of the whole document, and flags superseded specifications before they get cited.

Latest changelog:
https://github.com/shbernal/rfc-ai-tooling/releases/tag/v0.2.4

**关键词**: up, RFC, lookup, Look, IETF, RFCs, read, what

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/rfc-lookup)

---

## [24. Child Focus / Distraction Period Analysis | 儿童专注度与走神时段分析](https://clawhub.ai/smyx-sunjinhui/smyx-child-focus-analysis-analysis)

**Slug**: `smyx-child-focus-analysis-analysis`  
**Version**: 1.0.7  
**Stats**: ⭐ 0 | ⬇️ 757 | 🧩 8

**原始简介**: Using the camera built into a smart desk lamp or a tabletop camera, the system analyzes video of the child's study area in real time, detecting behavioral indicators such as face orientation (whether it deviates from the book/screen), eye gaze direction, and fidgeting hand actions (playing with a pen, touching the face, fiddling with objects), and computes a per-minute focus score (0-100) while recording distraction periods. The skill helps parents and teachers understand the child's learning state and optimize study habits. Application scenarios: smart study lamps, home study rooms, classrooms. The system monitors in real time, generates focus reports, and pushes alerts when focus stays persistently low. Skill features: improve learning efficiency. | 通过智能台灯内置摄像头或桌面摄像头，实时分析儿童学习区域的视频，检测面部朝向（是否偏离书本/屏幕）、眼部注视方向、手部小动作（玩笔、摸脸、摆弄物品）等行为指标，计算每分钟专注得分（0-100分），并记录走神时段。该技能可帮助家长和教师了解儿童学习状态，优化学习习惯。应用场景：智能学习台灯、家庭书房、教室。系统实时监测，生成专注度报告，当专注度持续偏低时推送提醒。技能特点：提升学习效率。

**中文介绍**: Using the camera built into a smart desk lamp or a tabletop camera, the system analyzes video of the child's study area in real time, detecting behavioral indicators such as face orientation (whether it deviates from the book/screen), eye gaze direction, and fidgeting hand actions (playing with a pen, touching the face, fiddling with objects), and computes a per-minute focus score (0-100) while recording distraction periods. The skill helps parents and teachers understand the child's learning state and optimize study habits. Application scenarios: smart study lamps, home study rooms, classrooms. The system monitors in real time, generates focus reports, and pushes alerts when focus stays persistently low. Skill features: improve learning efficiency. | 通过智能台灯内置摄像头或桌面摄像头，实时分析儿童学习区域的视频，检测面部朝向（是否偏离书本/屏幕）、眼部注视方向、手部小动作（玩笔、摸脸、摆弄物品）等行为指标，计算每分钟专注得分（0-100分），并记录走神时段。该技能可帮助家长和教师了解儿童学习状态，优化学习习惯。应用场景：智能学习台灯、家庭书房、教室。系统实时监测，生成专注度报告，当专注度持续偏低时推送提醒。技能特点：提升学习效率。

Latest changelog:
- Removed the file: skill-card.md.
- No functionality changes; documentation content remains the same.
- Housekeeping update to file structure.

**关键词**: 儿童专注度与走神时段分析, Child, Focus, Distraction, Period, Analysis, camera, built

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/smyx-child-focus-analysis-analysis)

---

## [25. agent4.io](https://clawhub.ai/hellojixian/agent4-io)

**Slug**: `agent4-io`  
**Version**: 1.1.9  
**Stats**: ⭐ 0 | ⬇️ 681 | 🧩 45

**原始简介**: Build and run grounded business agents on agent4.io over MCP — agents, knowledge bases, load-on-demand skills, stateful Storylines and page playbooks.

**中文介绍**: Build and run grounded business agents on agent4.io over MCP — agents, knowledge bases, load-on-demand skills, stateful Storylines and page playbooks.

Latest changelog:
Optional highlight_color: a second brand colour for the second chart series and citation markers, with foregrounds derived like the primary.

**关键词**: Agent, agent4.io, Build, run, grounded, business, over, MCP

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/agent4-io)

---

