#include QMK_KEYBOARD_H
#include "version.h"

//Tap Dance Declarations
enum {
	CT_RBR = 0, //Tap dance round brackets
	CT_SBR, //Tap dance square brackets
	CT_CBR, //Tap dance curly brackets
	CT_ABR, //Tap dance angle brackets
};

enum unicode_names {    
	AUM,
	OUM,
	UUM,
	AUM_S,
	OUM_S,
	UUM_S,
	ESZ,
	EUR
};

const uint32_t PROGMEM unicode_map[] = {    
	[AUM] = 0x00E4,
	[OUM] = 0x00F6,
	[UUM] = 0x00FC,
	[AUM_S] = 0x00C4,
	[OUM_S] = 0x00D6,
	[UUM_S] = 0x00DC,
	[ESZ] = 0x00DF,
	[EUR] = 0x20AC
};

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
	[0] = LAYOUT_ergodox_pretty(
		KC_ESC,    KC_1,      KC_2,      KC_3,      KC_4,           KC_5,      XP(ESZ, EUR),                     XP(UUM, UUM_S),      KC_6,         KC_7,         KC_8,         KC_9,         KC_0,      KC_NO,
		KC_NO,     KC_Q,      KC_W,      KC_E,      KC_R,           KC_T,      XP(AUM, AUM_S),                   XP(OUM, OUM_S),      KC_Y,         KC_U,         KC_I,         KC_O,         KC_SCLN,   KC_NO,
		KC_F12,    KC_A,      KC_S,      KC_D,      KC_F,           KC_G,                                                      				KC_H,         KC_J,         KC_K, 		    KC_L,   		  KC_P,      LT(2,KC_QUOT),
		KC_LSFT,   KC_Z,      KC_X,      KC_C,      KC_V,           KC_B,      KC_NO,                           KC_NO,   		        KC_N,         KC_M,         KC_COMM,      KC_DOT,       KC_MINS,   TG(3),
		KC_LCTL,   KC_LALT,   KC_LGUI,   KC_TILD,   LT(3,KC_SLSH),                                                                               KC_LGUI,			KC_LEFT,      KC_DOWN,      KC_UP,     KC_RGHT,
		                                                                       KC_DELETE,   KC_NO,   KC_NO,      KC_F23,
		                                                                                    KC_END,  KC_PGUP,
																																KC_SPC,    KC_BSPC,     KC_HOME, KC_PGDN,    LT(1,KC_TAB), KC_ENT
	),
	[1] = LAYOUT_ergodox_pretty(
		KC_NO,     KC_NO,     KC_NO,     KC_NO,     KC_NO,          KC_NO,    KC_NO,                           KC_NO,        KC_NO,        KC_NO,      KC_NO,     KC_NO,     KC_NO,   KC_NO,
		KC_NO,     KC_HASH,   KC_QUES,   KC_EXLM,   KC_AT,          KC_NO,    KC_NO,                           KC_NO,        KC_NO,        KC_NO,      KC_NO,     KC_NO,     KC_NO,   KC_NO,
		KC_NO,     KC_PIPE,   KC_SLSH,   KC_BSLS,   KC_GRAVE,       KC_NO,                                                   KC_NO,        TD(CT_RBR), TD(CT_SBR),TD(CT_CBR),TD(CT_ABR), KC_TRNS,
		KC_TRNS,   KC_PLUS,   KC_MINS,   KC_ASTR,  	KC_SLSH,        KC_EQL,   KC_NO,                           KC_NO,        KC_NO,        KC_NO,      KC_NO,     KC_NO,     KC_NO,   KC_TRNS,
		KC_NO,     KC_NO,     KC_EQL,    KC_TRNS,   KC_TRNS,                                                                               KC_NO,      KC_NO,     KC_NO,     KC_NO,   KC_NO,
		                                                                      KC_NO,  	KC_NO,   KC_NO,        KC_NO,
		                                                                                KC_NO,   KC_NO,
		                                                            KC_TRNS,  KC_TRNS,  KC_NO,   KC_NO,        KC_TRNS, KC_TRNS
	),
	[2] = LAYOUT_ergodox_pretty(
		KC_NO,     KC_F1,     KC_F2,     KC_F3,     KC_F4,          KC_F5,     KC_NO,                              KC_NO,        KC_F6,        KC_F7,      KC_F8,      KC_F9,     KC_F10,  KC_NO,
		KC_NO,     KC_NO,     KC_UP,     KC_NO,     KC_NO,          KC_NO,     KC_NO,                              KC_NO,        KC_NO,        KC_NO,      KC_NO,      KC_NO,     KC_NO,   KC_NO,
		KC_NO,     KC_LEFT,   KC_DOWN,   KC_RIGHT,  KC_NO,          KC_NO,                                                       KC_NO,        KC_NO,      KC_NO,      KC_NO,     KC_NO,   KC_TRNS,
		KC_NO,     KC_NO,     KC_NO,     KC_NO,     KC_NO,          KC_NO,     KC_NO,                              KC_NO,        KC_NO,        KC_NO,      KC_NO,      KC_NO,     KC_NO,   KC_NO,
		KC_NO,     KC_NO,     KC_NO,     KC_NO,     KC_NO,                                                                                     KC_NO,      KC_NO,      KC_NO,     KC_NO,   KC_NO,
		                                                                       RGB_SAI,     KC_NO,   KC_NO,        KC_NO,
		                                                                                    RGB_MOD, KC_NO,
		                                                            RGB_HUI,   RGB_VAI,     RGB_TOG, KC_NO,        KC_TRNS,      KC_TRNS
	),
	[3] = LAYOUT_ergodox_pretty(
		KC_TRNS,     KC_TRNS,     KC_TRNS,     KC_TRNS,     KC_TRNS,     KC_TRNS,   KC_TRNS,                          KC_TRNS,        KC_TRNS,        KC_NLCK,      KC_NO,        KC_NO,     KC_NO,     KC_NO,
		KC_TRNS,     KC_TRNS,     KC_TRNS,     KC_TRNS,     KC_TRNS,     KC_TRNS,   KC_TRNS,                          KC_TRNS,        KC_TRNS,        KC_P7,        KC_P8,        KC_P9,     KC_PAST,   KC_NO,
		KC_TRNS,     KC_TRNS,     KC_TRNS,     KC_TRNS,     KC_TRNS,     KC_TRNS,                                                     KC_PDOT,        KC_P4,        KC_P5,        KC_P6,     KC_PSLS,   KC_PEQL,
		KC_TRNS,     KC_TRNS,     KC_TRNS,     KC_TRNS,  	  KC_TRNS,     KC_TRNS,   KC_TRNS,                          KC_TRNS,        KC_TRNS,        KC_P1,        KC_P2,        KC_P3,     KC_PPLS,   KC_TRNS,
		KC_TRNS,     KC_TRNS,     KC_TRNS,     KC_TRNS,     KC_TRNS,                                                                                  KC_NO,        KC_NO,        KC_NO,     KC_PMNS,   KC_NO,
		                                                                            KC_TRNS,  KC_TRNS,   KC_TRNS,     KC_TRNS,
		                                                                                    	KC_TRNS,   KC_TRNS,
		                                                            		KC_TRNS,    KC_TRNS,  KC_TRNS,   KC_TRNS,     KC_TRNS, KC_TRNS
	)
};

qk_tap_dance_action_t tap_dance_actions[] = {
	[CT_RBR] = ACTION_TAP_DANCE_DOUBLE(KC_LPRN, KC_RPRN),
	[CT_SBR] = ACTION_TAP_DANCE_DOUBLE(KC_LBRC, KC_RBRC),
	[CT_CBR] = ACTION_TAP_DANCE_DOUBLE(KC_LCBR, KC_RCBR),
	[CT_ABR] = ACTION_TAP_DANCE_DOUBLE(KC_LABK, KC_RABK),
};

// Runs whenever there is a layer state change.
layer_state_t layer_state_set_user(layer_state_t state) {
	ergodox_right_led_1_off();
  ergodox_right_led_2_off();
  ergodox_right_led_3_off();

	uint8_t layer = get_highest_layer(state);
	switch (layer) {
		case 0:
			break;
		case 1:
			ergodox_right_led_1_on();
			ergodox_right_led_1_set(LED_BRIGHTNESS_LO);
			break;
		case 2:
			ergodox_right_led_1_on();
			ergodox_right_led_2_on();
			ergodox_right_led_1_set(LED_BRIGHTNESS_LO);
			ergodox_right_led_2_set(LED_BRIGHTNESS_LO);
		case 3:
			ergodox_right_led_1_on();
			ergodox_right_led_2_on();
			ergodox_right_led_3_on();
			ergodox_right_led_1_set(LED_BRIGHTNESS_LO);
			ergodox_right_led_2_set(LED_BRIGHTNESS_LO);
			ergodox_right_led_3_set(LED_BRIGHTNESS_LO);
			break;
	}
	return state;
};