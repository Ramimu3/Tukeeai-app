
import type { CustomThemeConfig } from '@skeletonlabs/tw-plugin';

export const myCustomTheme: CustomThemeConfig = {
    name: 'my-custom-theme',
    properties: {
		// =~= Theme Properties =~=
		"--theme-font-family-base": `system-ui`,
		"--theme-font-family-heading": `system-ui`,
		"--theme-font-color-base": "0 0 0",
		"--theme-font-color-dark": "255 255 255",
		"--theme-rounded-base": "9999px",
		"--theme-rounded-container": "8px",
		"--theme-border-base": "1px",
		// =~= Theme On-X Colors =~=
		"--on-primary": "255 255 255",
		"--on-secondary": "0 0 0",
		"--on-tertiary": "0 0 0",
		"--on-success": "0 0 0",
		"--on-warning": "0 0 0",
		"--on-error": "255 255 255",
		"--on-surface": "0 0 0",
		// =~= Theme Colors  =~=
		// primary | #407573 
		"--color-primary-50": "226 234 234", // #e2eaea
		"--color-primary-100": "217 227 227", // #d9e3e3
		"--color-primary-200": "207 221 220", // #cfdddc
		"--color-primary-300": "179 200 199", // #b3c8c7
		"--color-primary-400": "121 158 157", // #799e9d
		"--color-primary-500": "64 117 115", // #407573
		"--color-primary-600": "58 105 104", // #3a6968
		"--color-primary-700": "48 88 86", // #305856
		"--color-primary-800": "38 70 69", // #264645
		"--color-primary-900": "31 57 56", // #1f3938
		// secondary | #7ADFC7 
		"--color-secondary-50": "235 250 247", // #ebfaf7
		"--color-secondary-100": "228 249 244", // #e4f9f4
		"--color-secondary-200": "222 247 241", // #def7f1
		"--color-secondary-300": "202 242 233", // #caf2e9
		"--color-secondary-400": "162 233 216", // #a2e9d8
		"--color-secondary-500": "122 223 199", // #7ADFC7
		"--color-secondary-600": "110 201 179", // #6ec9b3
		"--color-secondary-700": "92 167 149", // #5ca795
		"--color-secondary-800": "73 134 119", // #498677
		"--color-secondary-900": "60 109 98", // #3c6d62
		// tertiary | #CF7438 
		"--color-tertiary-50": "248 234 225", // #f8eae1
		"--color-tertiary-100": "245 227 215", // #f5e3d7
		"--color-tertiary-200": "243 220 205", // #f3dccd
		"--color-tertiary-300": "236 199 175", // #ecc7af
		"--color-tertiary-400": "221 158 116", // #dd9e74
		"--color-tertiary-500": "207 116 56", // #CF7438
		"--color-tertiary-600": "186 104 50", // #ba6832
		"--color-tertiary-700": "155 87 42", // #9b572a
		"--color-tertiary-800": "124 70 34", // #7c4622
		"--color-tertiary-900": "101 57 27", // #65391b
		// success | #32b828 
		"--color-success-50": "224 244 223", // #e0f4df
		"--color-success-100": "214 241 212", // #d6f1d4
		"--color-success-200": "204 237 201", // #ccedc9
		"--color-success-300": "173 227 169", // #ade3a9
		"--color-success-400": "112 205 105", // #70cd69
		"--color-success-500": "50 184 40", // #32b828
		"--color-success-600": "45 166 36", // #2da624
		"--color-success-700": "38 138 30", // #268a1e
		"--color-success-800": "30 110 24", // #1e6e18
		"--color-success-900": "25 90 20", // #195a14
		// warning | #c19c2f 
		"--color-warning-50": "246 240 224", // #f6f0e0
		"--color-warning-100": "243 235 213", // #f3ebd5
		"--color-warning-200": "240 230 203", // #f0e6cb
		"--color-warning-300": "230 215 172", // #e6d7ac
		"--color-warning-400": "212 186 109", // #d4ba6d
		"--color-warning-500": "193 156 47", // #c19c2f
		"--color-warning-600": "174 140 42", // #ae8c2a
		"--color-warning-700": "145 117 35", // #917523
		"--color-warning-800": "116 94 28", // #745e1c
		"--color-warning-900": "95 76 23", // #5f4c17
		// error | #bd2837 
		"--color-error-50": "245 223 225", // #f5dfe1
		"--color-error-100": "242 212 215", // #f2d4d7
		"--color-error-200": "239 201 205", // #efc9cd
		"--color-error-300": "229 169 175", // #e5a9af
		"--color-error-400": "209 105 115", // #d16973
		"--color-error-500": "189 40 55", // #bd2837
		"--color-error-600": "170 36 50", // #aa2432
		"--color-error-700": "142 30 41", // #8e1e29
		"--color-error-800": "113 24 33", // #711821
		"--color-error-900": "93 20 27", // #5d141b
		// surface | #407573 
		"--color-surface-50": "226 234 234", // #e2eaea
		"--color-surface-100": "217 227 227", // #d9e3e3
		"--color-surface-200": "207 221 220", // #cfdddc
		"--color-surface-300": "179 200 199", // #b3c8c7
		"--color-surface-400": "121 158 157", // #799e9d
		"--color-surface-500": "64 117 115", // #407573
		"--color-surface-600": "58 105 104", // #3a6968
		"--color-surface-700": "48 88 86", // #305856
		"--color-surface-800": "38 70 69", // #264645
		"--color-surface-900": "40 42 41", // #1f3938
		
	}
}