def onCook(dat):
	op.raytk.mod.opDefinition.ensureExt(parent())
	ext.opDefinition.combineInputDefinitions(
		dat,
		inDats=dat.inputs,
		defFields=op('inlineFields'),
		supportedTypeTable=op('supportedTypes'),
		)
