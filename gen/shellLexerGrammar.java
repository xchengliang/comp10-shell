// Generated from C:/Users/MemoyMishra/Documents/UCL/year2_2023/softwareEngineering_COMP0010/comp0010-shell-python-p26/src/shellLexerGrammar.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class shellLexerGrammar extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		COMP_CMD=1, PIPE=2, SEMICOLON=3, QUOTE_SINGLE=4, QUOTE_DOUBLE=5, QUOTE_BACK=6, 
		REDIR_IN=7, REDIR_OUT=8, WHITESPACE=9, NEWLINE=10, QUOTED_STRING=11;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"COMP_CMD", "PIPE", "SEMICOLON", "QUOTE_SINGLE", "QUOTE_DOUBLE", "QUOTE_BACK", 
			"REDIR_IN", "REDIR_OUT", "WHITESPACE", "NEWLINE", "NON_KEYWORD_CHAR", 
			"NON_NEWLINE_NON_SINGLE_QUOTE", "NON_NEWLINE_NON_BACKQUOTE", "NON_NEWLINE_DOUBLE_QUOTE_CONTENT", 
			"NON_WHITESPACE", "COMAND", "ESCAPED_CHAR", "BACKQUOTED_STRING", "SINGLE_QUOTED_STRING", 
			"DOUBLE_QUOTED_STRING", "UNQUOTED_STRING", "QUOTED_STRING"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, "'|'", "';'", "'''", "'\"'", "'`'", "'<'", "'>'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "COMP_CMD", "PIPE", "SEMICOLON", "QUOTE_SINGLE", "QUOTE_DOUBLE", 
			"QUOTE_BACK", "REDIR_IN", "REDIR_OUT", "WHITESPACE", "NEWLINE", "QUOTED_STRING"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public shellLexerGrammar(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "shellLexerGrammar.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\u0004\u0000\u000b\u00b7\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002"+
		"\u0001\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002"+
		"\u0004\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002"+
		"\u0007\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002"+
		"\u000b\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e"+
		"\u0002\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011"+
		"\u0002\u0012\u0007\u0012\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014"+
		"\u0002\u0015\u0007\u0015\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0000\u0001\u0000\u0003\u0000_\b\u0000\u0001\u0001"+
		"\u0001\u0001\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0004"+
		"\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0007"+
		"\u0001\u0007\u0001\b\u0004\bp\b\b\u000b\b\f\bq\u0001\b\u0001\b\u0001\t"+
		"\u0003\tw\b\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\n\u0001\n\u0001\u000b"+
		"\u0001\u000b\u0001\f\u0001\f\u0001\r\u0001\r\u0001\u000e\u0001\u000e\u0001"+
		"\u000f\u0001\u000f\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0011\u0001"+
		"\u0011\u0001\u0011\u0005\u0011\u008f\b\u0011\n\u0011\f\u0011\u0092\t\u0011"+
		"\u0001\u0011\u0001\u0011\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012"+
		"\u0005\u0012\u009a\b\u0012\n\u0012\f\u0012\u009d\t\u0012\u0001\u0012\u0001"+
		"\u0012\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0005"+
		"\u0013\u00a6\b\u0013\n\u0013\f\u0013\u00a9\t\u0013\u0001\u0013\u0001\u0013"+
		"\u0001\u0014\u0004\u0014\u00ae\b\u0014\u000b\u0014\f\u0014\u00af\u0001"+
		"\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0003\u0015\u00b6\b\u0015\u0000"+
		"\u0000\u0016\u0001\u0001\u0003\u0002\u0005\u0003\u0007\u0004\t\u0005\u000b"+
		"\u0006\r\u0007\u000f\b\u0011\t\u0013\n\u0015\u0000\u0017\u0000\u0019\u0000"+
		"\u001b\u0000\u001d\u0000\u001f\u0000!\u0000#\u0000%\u0000\'\u0000)\u0000"+
		"+\u000b\u0001\u0000\u0007\u0002\u0000\t\t  \u0006\u0000\n\n\r\r\"\"\'"+
		"\';;||\u0003\u0000\n\n\r\r\'\'\u0003\u0000\n\n\r\r``\u0004\u0000\n\n\r"+
		"\r\"\"``\b\u0000\t\n\r\r  \"\"\'\';<>>||\u0002\u0000AZaz\u00c7\u0000\u0001"+
		"\u0001\u0000\u0000\u0000\u0000\u0003\u0001\u0000\u0000\u0000\u0000\u0005"+
		"\u0001\u0000\u0000\u0000\u0000\u0007\u0001\u0000\u0000\u0000\u0000\t\u0001"+
		"\u0000\u0000\u0000\u0000\u000b\u0001\u0000\u0000\u0000\u0000\r\u0001\u0000"+
		"\u0000\u0000\u0000\u000f\u0001\u0000\u0000\u0000\u0000\u0011\u0001\u0000"+
		"\u0000\u0000\u0000\u0013\u0001\u0000\u0000\u0000\u0000+\u0001\u0000\u0000"+
		"\u0000\u0001^\u0001\u0000\u0000\u0000\u0003`\u0001\u0000\u0000\u0000\u0005"+
		"b\u0001\u0000\u0000\u0000\u0007d\u0001\u0000\u0000\u0000\tf\u0001\u0000"+
		"\u0000\u0000\u000bh\u0001\u0000\u0000\u0000\rj\u0001\u0000\u0000\u0000"+
		"\u000fl\u0001\u0000\u0000\u0000\u0011o\u0001\u0000\u0000\u0000\u0013v"+
		"\u0001\u0000\u0000\u0000\u0015|\u0001\u0000\u0000\u0000\u0017~\u0001\u0000"+
		"\u0000\u0000\u0019\u0080\u0001\u0000\u0000\u0000\u001b\u0082\u0001\u0000"+
		"\u0000\u0000\u001d\u0084\u0001\u0000\u0000\u0000\u001f\u0086\u0001\u0000"+
		"\u0000\u0000!\u0088\u0001\u0000\u0000\u0000#\u008b\u0001\u0000\u0000\u0000"+
		"%\u0095\u0001\u0000\u0000\u0000\'\u00a0\u0001\u0000\u0000\u0000)\u00ad"+
		"\u0001\u0000\u0000\u0000+\u00b5\u0001\u0000\u0000\u0000-.\u0005c\u0000"+
		"\u0000._\u0005d\u0000\u0000/0\u0005p\u0000\u000001\u0005w\u0000\u0000"+
		"1_\u0005d\u0000\u000023\u0005l\u0000\u00003_\u0005s\u0000\u000045\u0005"+
		"c\u0000\u000056\u0005a\u0000\u00006_\u0005t\u0000\u000078\u0005e\u0000"+
		"\u000089\u0005c\u0000\u00009:\u0005h\u0000\u0000:_\u0005o\u0000\u0000"+
		";<\u0005h\u0000\u0000<=\u0005e\u0000\u0000=>\u0005a\u0000\u0000>_\u0005"+
		"d\u0000\u0000?@\u0005t\u0000\u0000@A\u0005a\u0000\u0000AB\u0005i\u0000"+
		"\u0000B_\u0005l\u0000\u0000CD\u0005g\u0000\u0000DE\u0005r\u0000\u0000"+
		"EF\u0005e\u0000\u0000F_\u0005p\u0000\u0000GH\u0005c\u0000\u0000HI\u0005"+
		"u\u0000\u0000I_\u0005t\u0000\u0000JK\u0005f\u0000\u0000KL\u0005i\u0000"+
		"\u0000LM\u0005n\u0000\u0000M_\u0005d\u0000\u0000NO\u0005u\u0000\u0000"+
		"OP\u0005n\u0000\u0000PQ\u0005i\u0000\u0000Q_\u0005q\u0000\u0000RS\u0005"+
		"s\u0000\u0000ST\u0005o\u0000\u0000TU\u0005r\u0000\u0000U_\u0005t\u0000"+
		"\u0000VW\u0005_\u0000\u0000WX\u0005l\u0000\u0000X_\u0005s\u0000\u0000"+
		"YZ\u0005_\u0000\u0000Z[\u0005g\u0000\u0000[\\\u0005r\u0000\u0000\\]\u0005"+
		"e\u0000\u0000]_\u0005p\u0000\u0000^-\u0001\u0000\u0000\u0000^/\u0001\u0000"+
		"\u0000\u0000^2\u0001\u0000\u0000\u0000^4\u0001\u0000\u0000\u0000^7\u0001"+
		"\u0000\u0000\u0000^;\u0001\u0000\u0000\u0000^?\u0001\u0000\u0000\u0000"+
		"^C\u0001\u0000\u0000\u0000^G\u0001\u0000\u0000\u0000^J\u0001\u0000\u0000"+
		"\u0000^N\u0001\u0000\u0000\u0000^R\u0001\u0000\u0000\u0000^V\u0001\u0000"+
		"\u0000\u0000^Y\u0001\u0000\u0000\u0000_\u0002\u0001\u0000\u0000\u0000"+
		"`a\u0005|\u0000\u0000a\u0004\u0001\u0000\u0000\u0000bc\u0005;\u0000\u0000"+
		"c\u0006\u0001\u0000\u0000\u0000de\u0005\'\u0000\u0000e\b\u0001\u0000\u0000"+
		"\u0000fg\u0005\"\u0000\u0000g\n\u0001\u0000\u0000\u0000hi\u0005`\u0000"+
		"\u0000i\f\u0001\u0000\u0000\u0000jk\u0005<\u0000\u0000k\u000e\u0001\u0000"+
		"\u0000\u0000lm\u0005>\u0000\u0000m\u0010\u0001\u0000\u0000\u0000np\u0007"+
		"\u0000\u0000\u0000on\u0001\u0000\u0000\u0000pq\u0001\u0000\u0000\u0000"+
		"qo\u0001\u0000\u0000\u0000qr\u0001\u0000\u0000\u0000rs\u0001\u0000\u0000"+
		"\u0000st\u0006\b\u0000\u0000t\u0012\u0001\u0000\u0000\u0000uw\u0005\r"+
		"\u0000\u0000vu\u0001\u0000\u0000\u0000vw\u0001\u0000\u0000\u0000wx\u0001"+
		"\u0000\u0000\u0000xy\u0005\n\u0000\u0000yz\u0001\u0000\u0000\u0000z{\u0006"+
		"\t\u0000\u0000{\u0014\u0001\u0000\u0000\u0000|}\b\u0001\u0000\u0000}\u0016"+
		"\u0001\u0000\u0000\u0000~\u007f\b\u0002\u0000\u0000\u007f\u0018\u0001"+
		"\u0000\u0000\u0000\u0080\u0081\b\u0003\u0000\u0000\u0081\u001a\u0001\u0000"+
		"\u0000\u0000\u0082\u0083\b\u0004\u0000\u0000\u0083\u001c\u0001\u0000\u0000"+
		"\u0000\u0084\u0085\b\u0005\u0000\u0000\u0085\u001e\u0001\u0000\u0000\u0000"+
		"\u0086\u0087\u0007\u0006\u0000\u0000\u0087 \u0001\u0000\u0000\u0000\u0088"+
		"\u0089\u0005\\\u0000\u0000\u0089\u008a\t\u0000\u0000\u0000\u008a\"\u0001"+
		"\u0000\u0000\u0000\u008b\u0090\u0003\u000b\u0005\u0000\u008c\u008f\u0003"+
		"\u0019\f\u0000\u008d\u008f\u0003#\u0011\u0000\u008e\u008c\u0001\u0000"+
		"\u0000\u0000\u008e\u008d\u0001\u0000\u0000\u0000\u008f\u0092\u0001\u0000"+
		"\u0000\u0000\u0090\u008e\u0001\u0000\u0000\u0000\u0090\u0091\u0001\u0000"+
		"\u0000\u0000\u0091\u0093\u0001\u0000\u0000\u0000\u0092\u0090\u0001\u0000"+
		"\u0000\u0000\u0093\u0094\u0003\u000b\u0005\u0000\u0094$\u0001\u0000\u0000"+
		"\u0000\u0095\u009b\u0003\u0007\u0003\u0000\u0096\u009a\u0003\u0017\u000b"+
		"\u0000\u0097\u009a\u0003!\u0010\u0000\u0098\u009a\u0003%\u0012\u0000\u0099"+
		"\u0096\u0001\u0000\u0000\u0000\u0099\u0097\u0001\u0000\u0000\u0000\u0099"+
		"\u0098\u0001\u0000\u0000\u0000\u009a\u009d\u0001\u0000\u0000\u0000\u009b"+
		"\u0099\u0001\u0000\u0000\u0000\u009b\u009c\u0001\u0000\u0000\u0000\u009c"+
		"\u009e\u0001\u0000\u0000\u0000\u009d\u009b\u0001\u0000\u0000\u0000\u009e"+
		"\u009f\u0003\u0007\u0003\u0000\u009f&\u0001\u0000\u0000\u0000\u00a0\u00a7"+
		"\u0003\t\u0004\u0000\u00a1\u00a6\u0003#\u0011\u0000\u00a2\u00a6\u0003"+
		"\u001b\r\u0000\u00a3\u00a6\u0003!\u0010\u0000\u00a4\u00a6\u0003\'\u0013"+
		"\u0000\u00a5\u00a1\u0001\u0000\u0000\u0000\u00a5\u00a2\u0001\u0000\u0000"+
		"\u0000\u00a5\u00a3\u0001\u0000\u0000\u0000\u00a5\u00a4\u0001\u0000\u0000"+
		"\u0000\u00a6\u00a9\u0001\u0000\u0000\u0000\u00a7\u00a5\u0001\u0000\u0000"+
		"\u0000\u00a7\u00a8\u0001\u0000\u0000\u0000\u00a8\u00aa\u0001\u0000\u0000"+
		"\u0000\u00a9\u00a7\u0001\u0000\u0000\u0000\u00aa\u00ab\u0003\t\u0004\u0000"+
		"\u00ab(\u0001\u0000\u0000\u0000\u00ac\u00ae\u0003\u001d\u000e\u0000\u00ad"+
		"\u00ac\u0001\u0000\u0000\u0000\u00ae\u00af\u0001\u0000\u0000\u0000\u00af"+
		"\u00ad\u0001\u0000\u0000\u0000\u00af\u00b0\u0001\u0000\u0000\u0000\u00b0"+
		"*\u0001\u0000\u0000\u0000\u00b1\u00b6\u0003%\u0012\u0000\u00b2\u00b6\u0003"+
		"\'\u0013\u0000\u00b3\u00b6\u0003#\u0011\u0000\u00b4\u00b6\u0003)\u0014"+
		"\u0000\u00b5\u00b1\u0001\u0000\u0000\u0000\u00b5\u00b2\u0001\u0000\u0000"+
		"\u0000\u00b5\u00b3\u0001\u0000\u0000\u0000\u00b5\u00b4\u0001\u0000\u0000"+
		"\u0000\u00b6,\u0001\u0000\u0000\u0000\f\u0000^qv\u008e\u0090\u0099\u009b"+
		"\u00a5\u00a7\u00af\u00b5\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}