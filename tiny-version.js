//super minimal & tiny version, does basicllly the same thing but no delay setting:

const generatePromoCodeLink=async()=>{const[t,o]=["https://api.discord.gx.games/v1/direct-fulfillment","1180231712274387115"],n=(()=>"xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx".replace(/[xy]/g,t=>(16*Math.random()|0).toString(16)))();try{const{token:e}=await(await fetch(t,{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({partnerUserId:n})})).json();return`https://discord.com/billing/partner-promotions/${o}/${e}`}catch(t){throw alert("Error"),t}},generateAndShowPromoUrl=async t=>{const o=[],n=async()=>{o.push(await generatePromoCodeLink()),o.length<t&&await n()};await n(),console.log(`${t}links:\n${o.join("\n")}`)};
generateAndShowPromoUrl(1); //replace the 1 with the number of links you wish to generate

// all the links generated are output'ed in console.
