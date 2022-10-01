const creator = alice.addr;
const defaultFrozen = true;
const unitName = "ALICEART";
const assetName = "tenx";

const url = "https://www.canva.com/design/DAFNojfu7nA/nAMb_G_JgZermdw06uYysw/edit?utm_content=DAFNojfu7nA&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton";
const managerAddr = undefined;
const reserveAddr = undefined;
const freezeAddr = undefined;
const clawbackAddr = undefined;
const total = 1; 
const decimals = 0; 
const txn = algosdk.makeAssetCreateTxnWithSuggestedParamsFromObject({
    from: creator,
    total,
    decimals,
    assetName,
    unitName,
    assetURL: url,
    assetMetadataHash: metadata,
    defaultFrozen,
    freeze: freezeAddr,
    manager: managerAddr,
    clawback: clawbackAddr,
    reserve: reserveAddr,
    suggestedParams: params,
});