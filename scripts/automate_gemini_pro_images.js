#!/usr/bin/env node

/**
 * Autonomous Gemini Pro Image Generation Bot using Chrome DevTools Protocol & Puppeteer
 * Connected to logged in user: sumanzfilms@gmail.com on port 9222
 */

const fs = require('fs');
const path = require('path');
const puppeteer = require('/Users/kalyan/Downloads/2026/Sep2026/Data Centers and Way Head/node_modules/puppeteer-core');

const BASE_DIR = path.resolve(__dirname, '..');
const ASSETS_DIR = path.join(BASE_DIR, 'assets');

if (!fs.existsSync(ASSETS_DIR)) {
  fs.mkdirSync(ASSETS_DIR, { recursive: true });
}

// Queue of 16:9 widescreen technological framework infographics
const queue = [
  {
    filename: "infographic_master_architecture_16x9.png",
    title: "NeerDrishti Assam Master Digital Twin Architecture",
    prompt: "A visionary 16:9 widescreen technological architectural framework infographic on a clean white and light-gray blueprint grid background illustrating NEERDRISHTI ASSAM: CANAL CONDITION MONITORING & PREDICTIVE MAINTENANCE CYBER-PHYSICAL DIGITAL TWIN ARCHITECTURE. The top dark navy header displays bold white typography with Government of Assam Irrigation Department NESFIC-D-02 badges. The visual presents 4 distinct horizontal engineered tiers: 1) Sensing & Edge Telemetry (Cantilevered IP68 Ultrasonic Level, Acoustic Doppler Flow, Vibrating-wire Embankment Piezometer Array, Solar 4G RTU); 2) Earth Observation & Autonomous UAV Patrols (Sentinel-2 10m NDWI Seepage Moisture Corridor, Drone RGB Crack & Slump Computer Vision); 3) Real-Time AI Digital Twin & Hydraulic Physics Engine (1D Saint-Venant Mass Balance Transit Loss Solver, Bishop Slope Stability Breach Forecasting Lead Time); 4) Departmental Governance & Field Automation (Assam State GIS Command Canvas, E-Nirman Automated SOR Work Orders, Farmer Water Equity Index). Metric badges: '+21% Water Efficiency', '<15min Seepage Flag', '14.5h Breach Lead Time', 'Rs 40L Grant'. Clean 2D flat vector aesthetic, deep teal, royal blue, cyan, emerald green, and gold accents, ultra-sharp engineering typography."
  },
  {
    filename: "infographic_hydraulic_loss_engine_16x9.png",
    title: "Saint-Venant Hydraulic Mass-Balance & Seepage Loss Localization",
    prompt: "A master engineering 16:9 widescreen technical diagnostic infographic on a clean white blueprint background with subtle technical gridlines illustrating SAINT-VENANT HYDRAULIC MASS-BALANCE & SEEPAGE LOSS LOCALIZATION ENGINE FOR IRRIGATION CANALS. Visualizing a longitudinal canal reach from Headworks Barrage (RD 0.0 km) to Tail-Reach Distributary (RD 28.5 km). Diagnostic callout cards showing Inflow (498.5 cusecs), Authorized Distributary Offtakes (185.0 cusecs), Tail Delivery (178.0 cusecs), Permissible Evaporative & Conveyance Loss (IS:9452), and Unaccounted Seepage Plume (62.5 cusecs at RD 9.1 km). Inset showing Sentinel-2 NDWI thermal moisture plume overlay. Clean vector design, dark navy, cyan, emerald green, and crimson alert badges, sharp mathematical notation."
  },
  {
    filename: "infographic_breach_forecasting_geotech_16x9.png",
    title: "Geotechnical Embankment Breach Prediction & Early Warning Horizon",
    prompt: "An authoritative 16:9 widescreen geotechnical engineering failure forecasting infographic on a clean light-gray blueprint grid background illustrating CANAL EMBANKMENT BREACH PREDICTION & BISHOP SLOPE STABILITY EARLY WARNING SYSTEM. Cutaway cross-section of an alluvial canal dyke showing soil pore-water pressure saturation during monsoon flood surge. Graph showing Factor of Safety (FoS) decaying from 1.45 (Stable) to 1.08 (Critical Breach Alert) with a prominent 14.5-Hour Predictive Lead Time milestone banner. Automated emergency upstream sluice gate throttling advisory card (-350 cusecs). Deep navy, amber, crimson, and gold accents, crisp engineering typography."
  },
  {
    filename: "infographic_cv_defect_matrix_16x9.png",
    title: "YOLOv8 & Mask-RCNN Canal Structural Defect Classification Matrix",
    prompt: "A high-contrast 16:9 widescreen AI computer vision defect classification matrix infographic on a clean white blueprint background illustrating YOLOV8 & MASK-RCNN CANAL STRUCTURAL DEFECT TRIAGE PIPELINE. 4 diagnostic inspection quadrants with high-resolution drone photo overlays and bounding boxes: 1) Embankment Scour & Slope Slump (96.4% confidence, 42 m3 soil loss); 2) Concrete Lining Fracture (92.1% confidence, 35mm crack aperture); 3) Aquatic Weed & Water Hyacinth Choke (98.2% confidence, 100% surface choke); 4) Silt Deposition Bed Rise (91.5% confidence, 0.85m silt rise). Automated remediation cards linked to Assam Irrigation Schedule of Rates (SOR). Professional 2D flat vector aesthetic."
  },
  {
    filename: "infographic_user_journey_workflow_16x9.png",
    title: "Paradigm Shift: Current Status Quo vs NeerDrishti Automated Loop",
    prompt: "A visionary 16:9 widescreen technological architectural infographic on a clean white and light-gray blueprint grid background illustrating PARADIGM SHIFT: CURRENT STATUS QUO VS. NEERDRISHTI AUTOMATED WORKFLOW FOR ASSAM IRRIGATION CANALS. Upper track shows the current manual routine in red and gray: foot patrols, 5-14 days paper delay, catastrophic breaches, emergency crisis tenders, parched tail farmers. Lower track shows NeerDrishti in emerald green and royal blue: edge IoT telemetry, <15 min anomaly alert, 14.5h breach forecasting, automated E-Nirman work-order, guaranteed tail-end water equity. Clean 2D flat vector aesthetic, ultra-sharp typography."
  },
  {
    filename: "infographic_roadmap_gantt_milestones_16x9.png",
    title: "7-Month Agile-V Development Roadmap & Validation Gates",
    prompt: "A master engineering roadmap infographic in 16:9 widescreen format on a clean white blueprint grid background illustrating 7-MONTH AGILE-V DEVELOPMENT ROADMAP & FIELD VALIDATION GATES FOR ASSAM CANALS. 7 monthly columns from Month 1 to Month 7 across 6 engineered tracks: Civil Survey, Edge IoT Firmware, AI Digital Twin, Web GIS Console, 30 km Field Pilot Deployment (Week 20 Validation Gate), and E-Nirman Handover. Vibrant color-coded milestone cards, diamonds, and progress bars. Clean 2D flat vector aesthetic, dark navy, cyan, emerald green, and amber gold."
  },
  {
    filename: "infographic_governance_security_16x9.png",
    title: "ASDC Cloud Architecture, Cybersecurity & Human-in-the-Loop",
    prompt: "An authoritative 16:9 widescreen cybersecurity and institutional governance infographic on a clean white blueprint background illustrating ASSAM STATE DATA CENTRE (ASDC) CLOUD DEPLOYMENT, CYBERSECURITY & HUMAN-IN-THE-LOOP GOVERNANCE FOR IRRIGATION AUTOMATION. 4 institutional pillars: 1) ASDC Sovereign Tier-III Cloud Hosting; 2) End-to-End TLS 1.3 & AES-256 Encryption; 3) Role-Based Access Control (RBAC) & Immutable Audit Trail; 4) Human-in-the-Loop Critical Safety Safeguard (No autonomous gate actuation or financial outlay without Executive Engineer digital sign-off). Clean 2D flat vector aesthetic, royal blue, emerald green, and gold accents."
  },
  {
    filename: "infographic_competitive_budget_16x9.png",
    title: "Competitive Differentiation & Rs 40 Lakhs Grant Resource Allocation",
    prompt: "A comprehensive 16:9 widescreen institutional technical infographic on a clean white blueprint background illustrating INNOVATION DIFFERENTIATION & RS 40.0 LAKHS GRANT RESOURCE ALLOCATION BREAKDOWN. Dual panel layout: Left panel features a competitive advantage matrix comparing manual visual patrols, generic satellite feeds, traditional SCADA, and NeerDrishti across detection speed, breach forecasting, and cost. Right panel features an itemized breakdown of the Rs. 40.0 Lakhs grant: Software Engineering Team (Rs. 20L - 50%), IoT Sensors (Rs. 11.5L - 28.8%), Field Survey & Mountings (Rs. 4L - 10%), Pilot & WUA Outreach (Rs. 2.5L - 6.2%), Cloud Infrastructure (Rs. 2L - 5%). Clean 2D flat vector design."
  },
  {
    filename: "wireframe_schematic.png",
    title: "State Canal Command Dashboard UI Wireframe",
    prompt: "A modern, high-tech 16:9 widescreen UI/UX architectural wireframe schematic on a clean dark navy and slate digital dashboard background illustrating NEERDRISHTI ASSAM STATE CANAL COMMAND DASHBOARD. Showing GIS interactive reach map of Jamuna and Dhansiri canal networks with color-coded chainages (green, yellow, red alert), real-time IoT sensor telemetry feed (ultrasonic water level, acoustic flow, dyke pore pressure), hydraulic mass balance loss meters, and automated E-Nirman work-order dispatch panel. Ultra-clean, modern government dashboard interface."
  },
  {
    filename: "iot_edge_hardware_schematic.png",
    title: "IoT Edge Telemetry Cantilevered Gantry & Piezometer Cross-Section",
    prompt: "An authoritative 16:9 widescreen engineering cutaway schematic on a clean white blueprint background illustrating IOT EDGE TELEMETRY TOPOLOGY: CANTILEVERED ULTRASONIC GANTRY & PIEZOMETER ARRAY FOR IRRIGATION CANAL DYKES. Architectural cross-section of a trapezoidal irrigation canal showing: 1) Overhanging steel cantilever post above 100-year High Flood Level; 2) 50W solar panel and IP68 LoRa/4G RTU gateway; 3) Non-contact ultrasonic water level transmitter emitting radar pulses to water surface; 4) Bed-mounted acoustic Doppler flow velocimeter; 5) Vibrating-wire piezometer embedded deep inside the earthen embankment toe measuring pore-water pressure. Crisp engineering CAD blueprint style, dark navy, cyan, and amber annotations."
  }
];

async function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function run() {
  console.log('\n=============================================================');
  console.log('🚀 AUTOMATED GEMINI PRO IMAGE GENERATION PIPELINE');
  console.log('👤 Account: sumanzfilms@gmail.com (Google Pro)');
  console.log(`📁 Target Assets Directory: ${ASSETS_DIR}`);
  console.log(`📋 Total Infographics in Queue: ${queue.length}`);
  console.log('=============================================================\n');

  let browser;
  try {
    browser = await puppeteer.connect({
      browserURL: 'http://127.0.0.1:9222',
      defaultViewport: null
    });
    console.log('✅ Connected to Google Chrome on port 9222!');
  } catch (err) {
    console.error('❌ Could not connect to Chrome on port 9222:', err.message);
    process.exit(1);
  }

  const pages = await browser.pages();
  let geminiPage = pages.find(p => p.url().includes('gemini.google.com'));

  if (!geminiPage) {
    console.log('🌐 Opening Gemini tab at https://gemini.google.com/app...');
    geminiPage = await browser.newPage();
    await geminiPage.goto('https://gemini.google.com/app', { waitUntil: 'networkidle2' });
  } else {
    console.log(`🌐 Using existing Gemini tab: ${geminiPage.url()}`);
    await geminiPage.bringToFront();
  }

  await sleep(2000);

  let successCount = 0;
  let failureCount = 0;

  for (let i = 0; i < queue.length; i++) {
    const item = queue[i];
    const targetFile = path.join(ASSETS_DIR, item.filename);

    console.log(`\n-------------------------------------------------------------`);
    console.log(`[${i + 1}/${queue.length}] 🎨 Generating: ${item.filename}`);
    console.log(`   🎯 Subject: ${item.title}`);
    console.log(`-------------------------------------------------------------`);

    let attempts = 0;
    let saved = false;

    while (attempts < 2 && !saved) {
      attempts++;
      try {
        // Record existing images in DOM
        const existingImageUrls = await geminiPage.evaluate(() => {
          return Array.from(document.querySelectorAll('img')).map(img => img.src).filter(Boolean);
        });

        // Click New Chat if available to keep context clean
        await geminiPage.evaluate(() => {
          const newChatBtn = document.querySelector('button[aria-label*=\"New chat\"], a[href*=\"/app\"], [data-test-id=\"new-chat-button\"]');
          if (newChatBtn) newChatBtn.click();
        }).catch(() => {});

        await sleep(1500);

        // Target input field
        const inputSelector = 'div.ql-editor, rich-textarea p, div[contenteditable=\"true\"]';
        await geminiPage.waitForSelector(inputSelector, { timeout: 15000 });

        const promptText = `Generate a high-impact, professional 16:9 widescreen technological framework infographic image: ${item.prompt}`;

        await geminiPage.evaluate((sel, text) => {
          const el = document.querySelector(sel);
          if (el) {
            el.focus();
            el.innerText = text;
            el.dispatchEvent(new Event('input', { bubbles: true }));
          }
        }, inputSelector, promptText);

        await sleep(800);

        // Click Send button or press Enter
        const sendClicked = await geminiPage.evaluate(() => {
          const btn = document.querySelector('button[aria-label*=\"Send\"], button.send-button, mat-icon[data-mat-icon-name=\"send\"]')?.closest('button');
          if (btn && !btn.disabled) {
            btn.click();
            return true;
          }
          return false;
        });

        if (!sendClicked) {
          await geminiPage.keyboard.press('Enter');
        }

        console.log(`   📤 Prompt submitted to Gemini. Waiting for generation...`);

        // Poll for new generated image in DOM
        let waitTime = 0;
        let imageBuffer = null;

        while (!imageBuffer && waitTime < 65) {
          await sleep(3000);
          waitTime += 3;

          const newImageData = await geminiPage.evaluate((existingUrls) => {
            const allImages = Array.from(document.querySelectorAll('img'));
            const candidates = allImages.filter(img => 
              img.src && 
              !existingUrls.includes(img.src) &&
              (img.src.includes('googleusercontent.com') || img.src.startsWith('blob:') || img.src.startsWith('data:image')) &&
              img.naturalWidth > 300
            );

            if (candidates.length > 0) {
              const latest = candidates[candidates.length - 1];
              if (latest.complete && latest.naturalWidth > 0) {
                try {
                  const canvas = document.createElement('canvas');
                  canvas.width = latest.naturalWidth;
                  canvas.height = latest.naturalHeight;
                  const ctx = canvas.getContext('2d');
                  ctx.drawImage(latest, 0, 0);
                  const dataUrl = canvas.toDataURL('image/png');
                  return { dataUrl: dataUrl.split(',')[1], width: latest.naturalWidth, height: latest.naturalHeight };
                } catch (e) {
                  return { src: latest.src, width: latest.naturalWidth, height: latest.naturalHeight };
                }
              }
            }
            return null;
          }, existingImageUrls);

          if (newImageData && newImageData.dataUrl) {
            console.log(`   🖼️ Captured image from canvas (${newImageData.width}x${newImageData.height})!`);
            imageBuffer = Buffer.from(newImageData.dataUrl, 'base64');
            break;
          }
        }

        if (imageBuffer) {
          fs.writeFileSync(targetFile, imageBuffer);
          const stats = fs.statSync(targetFile);
          console.log(`   ✅ Saved: assets/${item.filename} (${(stats.size / 1024).toFixed(1)} KB)`);
          saved = true;
          successCount++;
        } else {
          console.log(`   ⏳ No new image detected within 65s. Keeping current high-res vector infographic.`);
          failureCount++;
        }

      } catch (err) {
        console.error(`   ⚠️ Attempt ${attempts} error: ${err.message}`);
      }
    }

    if (i < queue.length - 1) {
      console.log(`   ⏳ Pausing 4s before next generation...`);
      await sleep(4000);
    }
  }

  console.log('\n=============================================================');
  console.log(`🎉 RUN FINISHED: ${successCount} generated via Gemini, ${failureCount} retained.`);
  console.log('=============================================================\n');

  browser.disconnect();
}

run().catch(err => {
  console.error('Fatal execution error:', err);
  process.exit(1);
});
