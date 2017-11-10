// Created by iWeb 3.0.4 local-build-20171110

setTransparentGifURL('Media/transparent.gif');function applyEffects()
{var registry=IWCreateEffectRegistry();registry.registerEffects({shadow_0:new IWShadow({blurRadius:4,offset:new IWPoint(1.4142,1.4142),color:'#000000',opacity:0.500000}),stroke_0:new IWStrokeParts([{rect:new IWRect(-1,1,2,173),url:'MetNum_files/stroke.png'},{rect:new IWRect(-1,-1,2,2),url:'MetNum_files/stroke_1.png'},{rect:new IWRect(1,-1,298,2),url:'MetNum_files/stroke_2.png'},{rect:new IWRect(299,-1,2,2),url:'MetNum_files/stroke_3.png'},{rect:new IWRect(299,1,2,173),url:'MetNum_files/stroke_4.png'},{rect:new IWRect(299,174,2,2),url:'MetNum_files/stroke_5.png'},{rect:new IWRect(1,174,298,2),url:'MetNum_files/stroke_6.png'},{rect:new IWRect(-1,174,2,2),url:'MetNum_files/stroke_7.png'}],new IWSize(300,175))});registry.applyEffects();}
function hostedOnDM()
{return false;}
function onPageLoad()
{loadMozillaCSS('MetNum_files/MetNumMoz.css')
adjustLineHeightIfTooBig('id1');adjustFontSizeIfTooBig('id1');adjustLineHeightIfTooBig('id2');adjustFontSizeIfTooBig('id2');adjustLineHeightIfTooBig('id3');adjustFontSizeIfTooBig('id3');Widget.onload();fixAllIEPNGs('Media/transparent.gif');applyEffects()}
function onPageUnload()
{Widget.onunload();}
